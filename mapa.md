- **Fecha:** 28/10/2026
- **Programa:** Anthropic en HackerOne
- **Fuente del alcance:** https://hackerone.com/anthropic
- **Objetivo del reconocimiento:** recopilar información pública sin realizar pruebas activas.

## 1. Registro del dominio

- **Dominio consultado:** claude.ai
- **Herramienta:** ICANN Lookup
- **Hallazgos:** registrador Markmonitor Inc.; nameservers isla.ns.cloudflare.com y randy.ns.cloudflare.com; datos del titular redactados por privacidad.

## 2. Registros DNS

- **Dominio consultado:** claude.ai
- **Herramienta:** dig
- **Hallazgos:**
  - A: 160.79.104.10
  - AAAA: 2607:6bc0::10
  - NS: isla.ns.cloudflare.com y randy.ns.cloudflare.com
  - MX: no se devolvieron registros MX en la consulta realizada.
  - TXT: seis registros, incluidos verificaciones de Google y SPF `v=spf1 -all`.
  - CAA: se devolvieron 18 registros.
- **Limitación:** resultados puntuales, sujetos a cambios.

## 3. Subdominios

- **Dominio consultado:** anthropic.com
- **Herramienta:** crt.sh
- **Ejemplos observados:** api.anthropic.com, api-staging.anthropic.com, console.anthropic.com, docs.anthropic.com, support.anthropic.com y status.anthropic.com.
- **Limitación:** la aparición en certificados no confirma que los hosts estén activos ni que estén autorizados para pruebas.

## 4. Huella tecnológica

- **Dominio consultado:** anthropic.com
- **Herramienta:** Netcraft Site Report
- **Hallazgos reportados:** Anthropic, PBC; Cloudflare; Google HTTPS Load Balancer; SignalPoint Communications como hosting indicado; tecnologías web como JavaScript y React Server Components.
- **Correo:** el informe muestra SPF y DMARC, con política DMARC `p=reject`.
- **Limitación:** las detecciones de terceros pueden ser incompletas o variar.

## 5. Ficheros públicos

- **Herramienta:** curl
- **robots.txt:** permite el rastreo general (`Allow: /`) y declara `https://www.anthropic.com/sitemap.xml`.
- **security.txt:** publica un contacto de HackerOne, la política de divulgación responsable, idioma preferido inglés y fecha de expiración declarada 2026-12-31.
- **Limitación:** estos archivos no son controles de acceso ni demuestran vulnerabilidades.

## 6. Servicios expuestos según fuentes públicas

- **IP consultada:** 160.79.104.10
- **Herramienta:** Shodan InternetDB
- **Nombres asociados:** claude.anthropic.com y a.anthropic.com.
- **CPE reportado:** cloudflare:cloudflare.
- **Puertos listados por la fuente:** 80, 443, 2052, 2082, 2083, 2086, 2087, 2096, 8080, 8443 y 8880.
- **Vulnerabilidades listadas:** ninguna.
- **Limitación:** no se verificó el estado actual de los puertos ni se realizaron conexiones o escaneos.

## 7. Google dorks

- **Consulta:** `site:anthropic.com filetype:pdf`
- **Hallazgos:** varios PDF indexados, incluidos informes corporativos, documentos de investigación y publicaciones sobre seguridad de IA.
- **Limitación:** la indexación pública no implica exposición indebida.

## 8. Correos y datos públicos de contacto

- **Herramienta:** theHarvester 4.11.1
- **Comando:** `theHarvester -d anthropic.com -b crtsh`
- **Resultado:** la fuente consultada no devolvió IPs, correos, personas ni hosts.
- **Limitación:** la ausencia de resultados no demuestra que no existan correos públicos.

## Evaluación general

Este mapa resume resultados obtenidos mediante fuentes públicas y técnicas de reconocimiento pasivo. No se han confirmado vulnerabilidades. Los nombres y servicios descubiertos deben contrastarse individualmente con el alcance vigente del programa HackerOne antes de cualquier actividad adicional.

No se realizaron escaneos activos, explotación, fuerza bruta ni intentos de acceso a datos privados.