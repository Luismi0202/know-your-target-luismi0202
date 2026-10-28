# Cuaderno de reconocimiento pasivo

## Registro 1 — Preparación del alcance

- **Fecha:** 28/10/2026
- **Hora:** 12:39
- **Objetivo:** Inventario inicial de activos de Anthropic.
- **Técnica:** Revisión de la política y del CSV público de HackerOne.
- **Fuente:** https://hackerone.com/anthropic
- **Acción:** Revisé las directrices del programa y seleccioné hosts para el reconocimiento pasivo.
- **Resultado:** Se creó `scope.txt` con siete hosts para la revisión inicial.
- **Limitaciones:** La inclusión en este listado no autoriza pruebas activas. Se respetarán las instrucciones específicas de cada activo.
- **Siguiente paso:** Consultar información WHOIS pública y registrar los resultados.

## Registro 2 — WHOIS de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 12:50, hora local aproximada
- **Objetivo:** claude.ai
- **Técnica:** Consulta registral pasiva mediante ICANN Lookup.
- **Fuente:** https://lookup.icann.org/
- **Acción:** Consulté los datos públicos del registro del dominio.
- **Resultado observado:**
  - Registrador: Markmonitor Inc.
  - Creación: 2018-08-04.
  - Expiración: 2029-08-04.
  - Última actualización indicada: 2026-08-12.
  - Nameservers: isla.ns.cloudflare.com y randy.ns.cloudflare.com.
  - Estados: clientDeleteProhibited, clientTransferProhibited y clientUpdateProhibited.
  - DNSSEC: la delegación aparece como Unsigned.
  - Los datos de contacto del titular aparecen redactados por privacidad.
- **Interpretación:** El dominio utiliza nameservers de Cloudflare. Los datos del titular no están disponibles en el resultado consultado. No se ha identificado ninguna vulnerabilidad mediante esta consulta.
- **Limitación:** El comando whois desde Kali devolvió Network is unreachable; se utilizó ICANN Lookup como alternativa web.
- **Siguiente paso:** Consultar los registros DNS públicos.

## Registro 3 — DNS A de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 11:52 UTC
- **Objetivo:** claude.ai
- **Técnica:** Consulta DNS pasiva mediante dig.
- **Comando:** dig claude.ai A
- **Resultado observado:** NOERROR; se obtuvo un registro A con la dirección IPv4 160.79.104.10 y TTL de 300 segundos.
- **Servidor DNS consultado:** 8.8.8.8.
- **Tiempo de consulta:** 21 ms.
- **Interpretación:** La consulta devolvió una dirección IPv4 para el dominio en el momento de la observación.
- **Limitación:** Una única consulta no permite afirmar que sea la única dirección IP asociada al dominio.
- **Siguiente paso:** Consultar el registro MX para comprobar si el dominio publica información de servidores de correo.

## Registro 4 — DNS MX de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 11:57 UTC
- **Objetivo:** claude.ai
- **Técnica:** Consulta DNS pasiva mediante dig.
- **Comando:** dig claude.ai MX
- **Resultado observado:** Estado NOERROR, ANSWER: 0. No se devolvieron registros MX. La sección AUTHORITY contiene un registro SOA que identifica isla.ns.cloudflare.com como servidor primario indicado.
- **Servidor DNS consultado:** 8.8.8.8.
- **Tiempo de consulta:** 23 ms.
- **Interpretación:** La consulta no devolvió registros MX para claude.ai en el momento de la observación.
- **Limitación:** Este resultado no permite concluir que Anthropic carezca de servicios de correo.
- **Siguiente paso:** Consultar el registro TXT público del dominio.

## Registro 5 — DNS TXT de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 11:59 UTC
- **Objetivo:** claude.ai
- **Técnica:** Consulta DNS pasiva mediante dig.
- **Comando:** dig claude.ai TXT
- **Resultado observado:** NOERROR; se devolvieron 6 registros TXT, todos con TTL de 300 segundos.
- **Contenido observado:** Cuatro registros google-site-verification, un registro SPF con valor "v=spf1 -all" y una cadena TXT adicional cuyo propósito no se ha determinado.
- **Servidor DNS consultado:** 8.8.8.8.
- **Tiempo de consulta:** 14 ms.
- **Interpretación:** El dominio publica valores de verificación y una política SPF que indica que ningún servidor está autorizado a enviar correo usando esa identidad SPF.
- **Limitación:** No se ha verificado el propósito de la cadena adicional ni se han probado los mecanismos de verificación.
- **Siguiente paso:** Consultar los registros CAA públicos del dominio.

## Registro 6 — DNS CAA de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 12:02 UTC
- **Objetivo:** claude.ai
- **Técnica:** Consulta DNS pasiva mediante dig.
- **Comando:** dig claude.ai CAA
- **Resultado observado:** NOERROR; se devolvieron 18 registros CAA, con TTL de 300 segundos.
- **Contenido observado:** Registros issue e issuewild que mencionan distintas autoridades certificadoras, entre ellas Let's Encrypt, DigiCert, Amazon, SSL.com, Google PKI y otras.
- **Servidor DNS consultado:** 8.8.8.8.
- **Tiempo de consulta:** 16 ms.
- **Interpretación:** El dominio publica una política CAA que enumera autoridades certificadoras para la emisión de certificados normales y wildcard.
- **Limitación:** La consulta no verifica certificados emitidos ni demuestra vulnerabilidades.
- **Siguiente paso:** Consultar los registros AAAA públicos del dominio.

## Registro 7 — DNS AAAA de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 12:04 UTC
- **Objetivo:** claude.ai
- **Técnica:** Consulta DNS pasiva mediante dig.
- **Comando:** dig claude.ai AAAA
- **Resultado observado:** NOERROR; se devolvió una dirección IPv6: 2607:6bc0::10, con TTL de 300 segundos.
- **Servidor DNS consultado:** 8.8.8.8.
- **Tiempo de consulta:** 25 ms.
- **Interpretación:** El dominio publicó una dirección IPv6 en el momento de la consulta. También se había observado una dirección IPv4 en la consulta A.
- **Limitación:** Los resultados corresponden a una observación puntual y pueden cambiar.
- **Siguiente paso:** Revisar los registros NS del dominio.

## Registro 8 — DNS NS de claude.ai

- **Fecha:** 28/10/2026
- **Hora:** 12:06 UTC
- **Objetivo:** claude.ai
- **Técnica:** Consulta DNS pasiva mediante dig.
- **Comando:** dig claude.ai NS
- **Resultado observado:** NOERROR; se devolvieron dos registros NS: isla.ns.cloudflare.com y randy.ns.cloudflare.com.
- **TTL:** 21600 segundos para ambos registros.
- **Servidor DNS consultado:** 8.8.8.8.
- **Tiempo de consulta:** 19 ms.
- **Interpretación:** Los servidores de nombres observados coinciden con los indicados en la consulta ICANN Lookup.
- **Limitación:** La consulta identifica servidores DNS, pero no demuestra la existencia ni ausencia de vulnerabilidades.
- **Siguiente paso:** Consultar el registro SOA del dominio.

## Registro 9 — Descubrimiento pasivo de subdominios

- **Fecha:** 28/10/2026
- **Objetivo:** anthropic.com
- **Técnica:** Consulta de certificados TLS públicos mediante crt.sh.
- **Fuente:** https://crt.sh/?q=%25.anthropic.com
- **Comando utilizado:** curl -s 'https://crt.sh/?q=%25.anthropic.com&output=json' | python3 -c 'import sys,json; d=json.load(sys.stdin); print("\n".join(sorted({x["name_value"] for x in d if x.get("name_value")})))'
- **Resultado observado:** Se obtuvieron numerosos nombres de dominio y subdominio, con duplicados eliminados por el comando y algunos nombres wildcard.
- **Ejemplos encontrados:** api.anthropic.com, api-staging.anthropic.com, console.anthropic.com, docs.anthropic.com, support.anthropic.com, status.anthropic.com y www.anthropic.com.
- **Interpretación:** Los certificados públicos permiten identificar nombres asociados a la infraestructura y servicios de Anthropic.
- **Limitación:** Los resultados no confirman que todos los nombres estén activos ni que pertenezcan al alcance autorizado. Se contrastarán con scope.txt y la política del programa.
- **Siguiente paso:** Revisar la huella tecnológica con Netcraft.

## Registro 10 — Huella tecnológica con Netcraft

- **Fecha:** 28/10/2026
- **Objetivo consultado:** anthropic.com
- **Técnica:** Fingerprinting pasivo mediante Netcraft Site Report.
- **Fuente:** https://sitereport.netcraft.com/
- **Resultado observado:** Netcraft identifica Anthropic, PBC como propietario del bloque de red. Indica SignalPoint Communications como empresa de hosting, Cloudflare como CDN/DNS y Google HTTPS Load Balancer como tecnología de aceleración HTTP.
- **Direcciones observadas:** IPv4 160.79.104.10 e IPv6 2607:6bc0::10.
- **DNS:** isla.ns.cloudflare.com; el informe indica DNSSEC habilitado para el dominio consultado.
- **Correo:** el informe muestra SPF con include de _spf.google.com y softfail, además de DMARC con políticas p=reject y sp=reject.
- **Otras tecnologías detectadas:** JavaScript, React Server Components, gzip y varias cabeceras de seguridad del navegador.
- **Interpretación:** La fuente ofrece indicios sobre infraestructura, entrega de contenido y tecnologías web de anthropic.com.
- **Limitación:** Son detecciones de terceros y pueden ser incompletas o variar con el tiempo. El informe consultado indica que la página HTTP no es HTTPS; no se ha comprobado aquí el informe HTTPS ni se han realizado pruebas activas.
- **Siguiente paso:** Revisar robots.txt y security.txt de forma pasiva.

## Registro 11 — Consulta de robots.txt

- **Fecha:** 28/10/2026
- **Objetivo:** anthropic.com
- **Técnica:** Revisión pasiva de robots.txt.
- **Comando:** curl -sS -L --max-time 15 https://anthropic.com/robots.txt
- **Resultado observado:** User-Agent: *, Allow: / y Sitemap: https://www.anthropic.com/sitemap.xml.
- **Interpretación:** El archivo permite el rastreo general y declara la ubicación del sitemap.
- **Limitación:** robots.txt no es un mecanismo de control de acceso ni confirma que no existan otras rutas.
- **Siguiente paso:** Consultar security.txt en la ubicación estándar.

## Registro 12 — Consulta de security.txt

- **Fecha:** 28/10/2026
- **Objetivo:** anthropic.com
- **Técnica:** Revisión pasiva del archivo security.txt.
- **Comando:** curl -sS -L --max-time 15 https://anthropic.com/.well-known/security.txt
- **Resultado observado:** El archivo declara un contacto de HackerOne, fecha de expiración 2026-12-31T23:59:00.000Z, idioma preferido inglés, URL canónica, política de divulgación responsable y página de empleo.
- **Interpretación:** Anthropic publica un canal para reportar vulnerabilidades y una política asociada.
- **Limitación:** La presencia de estos enlaces no implica que se haya enviado un informe ni que se haya validado ninguna vulnerabilidad.
- **Siguiente paso:** Consultar información pública de servicios mediante Shodan InternetDB, sin escanear el objetivo.

## Registro 13 — Shodan InternetDB

- **Fecha:** 28/10/2026
- **Objetivo:** IP 160.79.104.10, obtenida previamente mediante DNS.
- **Técnica:** Consulta pasiva de información pública con Shodan InternetDB.
- **Fuente:** https://internetdb.shodan.io/160.79.104.10
- **Comando:** curl -sS --max-time 15 https://internetdb.shodan.io/160.79.104.10
- **Resultado observado:** La respuesta JSON enumera los nombres claude.anthropic.com y a.anthropic.com, el CPE cpe:/a:cloudflare:cloudflare, los puertos 80, 443, 2052, 2082, 2083, 2086, 2087, 2096, 8080, 8443 y 8880, la etiqueta pqc y una lista vacía de vulnerabilidades.
- **Interpretación:** La fuente asocia la IP con Cloudflare y publica metadatos de servicios y nombres relacionados.
- **Limitación:** Los datos de InternetDB pueden estar incompletos o desactualizados. No se realizaron conexiones a los puertos ni pruebas de vulnerabilidad.
- **Siguiente paso:** Realizar búsquedas públicas mediante Google dorks.

## Registro 14 — Google dorks: documentos PDF

- **Fecha:** 28/10/2026
- **Objetivo:** anthropic.com
- **Técnica:** Búsqueda pasiva mediante Google dorks.
- **Consulta:** site:anthropic.com filetype:pdf
- **Resultado observado:** Se encontraron varios PDF indexados, incluidos informes corporativos, documentos de investigación y publicaciones sobre seguridad de IA. Algunos resultados utilizan el dominio www-cdn.anthropic.com.
- **Interpretación:** Los motores de búsqueda permiten identificar documentos publicados bajo dominios asociados a Anthropic.
- **Limitación:** La indexación pública no demuestra una exposición indebida. No se descargaron ni analizaron documentos potencialmente sensibles.
- **Siguiente paso:** Buscar información de contacto corporativa mediante fuentes públicas.

## Registro 15 — Búsqueda pasiva de correos con theHarvester

- **Fecha:** 28/10/2026
- **Objetivo:** anthropic.com
- **Técnica:** Recopilación pasiva de información pública.
- **Herramienta:** theHarvester 4.11.1.
- **Comando:** theHarvester -d anthropic.com -b crtsh
- **Fuente consultada:** CRTsh.
- **Resultado observado:** No se encontraron direcciones IP, correos electrónicos, personas ni hosts en esta consulta.
- **Interpretación:** La fuente consultada no devolvió resultados para esos campos en esta ejecución.
- **Limitación:** La ausencia de resultados no demuestra que no existan correos o hosts públicos.
- **Siguiente paso:** Revisar que los resultados estén reflejados en el mapa de reconocimiento.

