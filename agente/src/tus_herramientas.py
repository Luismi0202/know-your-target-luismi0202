"""Herramientas iniciales de reconocimiento. AQUÍ PUEDES AÑADIR LAS TUYAS.

WHOIS (whois.py), DNS y crt.sh ya están implementadas y activas en lanzar.py.
DNS y crt.sh proceden de la solución del profesor (herramientas/recon.py).

Añadidas desde el cuaderno de reconocimiento pasivo (solo las de terminal):
robots_txt, security_txt, shodan_internetdb y correos_theharvester; además
dns_registros ya admite el tipo CAA. Google dorks y Netcraft se quedan fuera
por ser consultas de navegador, no de terminal.

Para ampliar: una tarea por función, @protegida, sin shell, con timeout,
salida recortada, errores como texto y resultados filtrados por el alcance.
Importa tu nueva función en lanzar.py y añádela a HERRAMIENTAS.

Ideas: subdominios_subfinder, wayback_urls, infraestructura_ip,
correo_postura (SPF/DMARC/MTA-STS/CAA), urlscan.
"""

import ipaddress
import json
import subprocess
import urllib.error
import urllib.parse
import urllib.request

from guard import protegida, filtrar
from alcance import normalizar
from whois import recortar

UA = "aap-recon/1.0 (educativo; IES Rafael Alberti)"
TIPOS_DNS = {"A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA", "CAA"}


def _http(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


@protegida(objetivo="dominio")
def dns_registros(dominio: str, tipo: str = "A") -> str:
    """Consulta registros DNS de un dominio. tipo: A, AAAA, MX, NS, TXT, CNAME,
    SOA o CAA. Devuelve los valores, uno por línea."""
    tipo = tipo.upper()
    if tipo not in TIPOS_DNS:
        return f"ERROR: tipo DNS no válido ({tipo}). Usa uno de: {', '.join(sorted(TIPOS_DNS))}."
    try:
        r = subprocess.run(["dig", "+short", tipo, dominio],
                           capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return "ERROR: dig no respondió en 20 segundos."
    except OSError as e:
        return recortar(f"ERROR: no se pudo ejecutar dig: {e}")
    if r.returncode != 0:
        return recortar(f"ERROR: dig falló ({r.returncode}): {r.stderr.strip() or 'sin detalles'}")
    salida = recortar(r.stdout.strip())
    return salida or f"Sin registros {tipo} para {dominio}."


@protegida(objetivo="dominio")
def subdominios_crtsh(dominio: str) -> str:
    """Enumera subdominios de un dominio por transparencia de certificados (crt.sh).
    Pasivo: no toca el objetivo. Devuelve solo los subdominios dentro del alcance."""
    url = f"https://crt.sh/?q=%25.{urllib.parse.quote(dominio)}&output=json"
    try:
        datos = json.loads(_http(url, timeout=90))
    except Exception as e:
        return (f"ERROR: crt.sh no respondió ({e}). crt.sh suele ir lento; "
                "puedes reintentar más tarde o añadir otra fuente de subdominios.")
    if not isinstance(datos, list) or any(
        not isinstance(fila, dict) or not isinstance(fila.get("name_value"), str)
        for fila in datos
    ):
        return "ERROR: crt.sh devolvió un formato de certificados inesperado."
    nombres = set()
    for fila in datos:
        for n in str(fila.get("name_value", "")).splitlines():
            n = n.strip().lstrip("*.").lower()
            if n:
                nombres.add(n)
    dentro, fuera = filtrar(sorted(nombres))
    cab = f"{len(dentro)} subdominios en alcance ({fuera} filtrados por estar fuera):\n"
    return recortar(cab + "\n".join(dentro))


@protegida(objetivo="dominio")
def robots_txt(dominio: str) -> str:
    """Descarga el archivo robots.txt público de un dominio (por HTTPS) para ver
    qué rutas y sitemaps anuncia. No es un control de acceso. Devuelve su contenido."""
    host = normalizar(dominio)
    url = f"https://{host}/robots.txt"
    try:
        texto = _http(url, timeout=15)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"{host} no publica /robots.txt (HTTP 404)."
        return f"ERROR: {host} devolvió HTTP {e.code} al pedir /robots.txt."
    except Exception as e:
        return recortar(f"ERROR: no se pudo descargar robots.txt de {host}: {e}")
    texto = texto.strip()
    return recortar(texto) if texto else f"{host} devolvió un robots.txt vacío."


@protegida(objetivo="dominio")
def security_txt(dominio: str) -> str:
    """Descarga el security.txt de un dominio (RFC 9116): canal de contacto y
    política para reportar vulnerabilidades. Prueba /.well-known/ y la raíz."""
    host = normalizar(dominio)
    ubicaciones = (f"https://{host}/.well-known/security.txt",
                   f"https://{host}/security.txt")
    errores = []
    for url in ubicaciones:
        try:
            texto = _http(url, timeout=15).strip()
        except urllib.error.HTTPError as e:
            errores.append(f"{url} -> HTTP {e.code}")
            continue
        except Exception as e:
            errores.append(f"{url} -> {e}")
            continue
        if texto:
            return recortar(f"[{url}]\n{texto}")
    return f"{host} no publica security.txt. Intentos: " + "; ".join(errores)


@protegida(objetivo="ip")
def shodan_internetdb(ip: str) -> str:
    """Consulta datos públicos de una IP en Shodan InternetDB: puertos, nombres,
    CPE, etiquetas y CVE conocidos. Pasivo: no conecta con la IP, solo lee la base
    de Shodan. La IP debe estar dentro del alcance autorizado."""
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return f"ERROR: '{ip}' no es una IP válida. Obtén primero la IP con dns_registros."
    try:
        datos = json.loads(_http(f"https://internetdb.shodan.io/{ip}", timeout=20))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Shodan InternetDB no tiene datos para {ip}."
        return f"ERROR: Shodan InternetDB devolvió HTTP {e.code} para {ip}."
    except Exception as e:
        return recortar(f"ERROR: no se pudo consultar Shodan InternetDB: {e}")
    if not isinstance(datos, dict):
        return "ERROR: Shodan InternetDB devolvió un formato inesperado."
    puertos = datos.get("ports") or []
    nombres = datos.get("hostnames") or []
    cpes = datos.get("cpes") or []
    etiquetas = datos.get("tags") or []
    vulns = datos.get("vulns") or []
    lineas = [
        f"IP: {ip}",
        f"Puertos: {', '.join(map(str, puertos)) or 'ninguno'}",
        f"Nombres: {', '.join(nombres) or 'ninguno'}",
        f"CPE: {', '.join(cpes) or 'ninguno'}",
        f"Etiquetas: {', '.join(etiquetas) or 'ninguna'}",
        f"Vulnerabilidades (CVE): {', '.join(vulns) or 'ninguna'}",
    ]
    return recortar("\n".join(lineas))


@protegida(objetivo="dominio")
def correos_theharvester(dominio: str) -> str:
    """Recopila correos y hosts públicos de un dominio con theHarvester usando la
    fuente pasiva crt.sh. Requiere theHarvester instalado en el sistema."""
    for binario in ("theHarvester", "theharvester"):
        try:
            r = subprocess.run([binario, "-d", dominio, "-b", "crtsh"],
                               capture_output=True, text=True, timeout=120)
        except FileNotFoundError:
            continue
        except subprocess.TimeoutExpired:
            return "ERROR: theHarvester no respondió en 120 segundos."
        except OSError as e:
            return recortar(f"ERROR: no se pudo ejecutar theHarvester: {e}")
        salida = (r.stdout or "").strip()
        if r.returncode != 0 and not salida:
            detalle = (r.stderr or "").strip()[:200] or "sin detalles"
            return recortar(f"ERROR: theHarvester falló ({r.returncode}): {detalle}")
        return recortar(salida or f"theHarvester no devolvió resultados para {dominio}.")
    return "ERROR: theHarvester no está instalado en este sistema."
