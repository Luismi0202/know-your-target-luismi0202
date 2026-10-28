# Proyecto 1 — Know Your Target

## Autor
[Tu nombre o identificador académico]

## Objetivo
Anthropic

## Programa
Anthropic — HackerOne Bug Bounty Program

## Política
https://hackerone.com/anthropic

## Fecha de consulta
2026-10-28

## Alcance
Se preparó una lista inicial de siete hosts identificados en la información del programa:

- `claude.ai`
- `api.anthropic.com`
- `api-staging.anthropic.com`
- `console.anthropic.com`
- `docs.anthropic.com`
- `support.anthropic.com`
- `anthropic.atlassian.com`

La lista se encuentra en `scope.txt`. Los hosts se registraron como candidatos para el inventario inicial; su inclusión en esta lista no implica autorización general para realizar pruebas. Antes de cualquier actividad adicional se debe comprobar el alcance y las restricciones vigentes del programa.

Se identificó `https://github.com/modelcontextprotocol` como excluido según la información del programa consultada. Los servicios de terceros no se consideran automáticamente dentro del alcance. Las pruebas de seguridad de modelos, como jailbreaks, se encuentran fuera del programa de infraestructura descrito.

## Metodología
Se realizó reconocimiento pasivo mediante fuentes públicas y consultas de lectura, sin intentar explotar vulnerabilidades ni acceder a datos privados.

Técnicas utilizadas:

1. **Registro de dominio:** consulta de ICANN Lookup para `claude.ai`, al no funcionar la consulta WHOIS desde la terminal.
2. **Registros DNS:** consultas `dig` para A, AAAA, NS, MX, TXT y CAA.
3. **Subdominios:** consulta de certificados públicos mediante `crt.sh` para `anthropic.com`.
4. **Huella tecnológica:** consulta del informe de Netcraft para `anthropic.com`.
5. **Ficheros públicos:** consulta de `robots.txt` y `security.txt`.
6. **Servicios expuestos en fuentes públicas:** consulta de Shodan InternetDB para la IP `160.79.104.10`, sin escanear puertos.
7. **Google dorks:** búsqueda de documentos PDF indexados mediante `site:anthropic.com filetype:pdf`.
8. **Correos y metadatos públicos:** ejecución de `theHarvester` usando la fuente `crtsh`.

No se realizaron escaneos activos, fuerza bruta, explotación, ingeniería social ni intentos de acceso a información privada. No se crearon cuentas en los sistemas de la organización.

## Documentos
- `alcance.md`: reglas, restricciones y alcance normalizado.
- `scope.txt`: lista inicial de siete hosts para el inventario.
- `cuaderno.md`: registro de comandos, fuentes, resultados y observaciones.
- `mapa.md`: resumen de la superficie de ataque observada mediante fuentes públicas.
- `comparativa.md`: comparación con el agente de IA, pendiente de completar cuando se disponga de sus resultados.

## Resultados

### 1. Registro de dominio
Para `claude.ai`, ICANN Lookup indicó Markmonitor Inc. como registrador y los nameservers `isla.ns.cloudflare.com` y `randy.ns.cloudflare.com`. Los datos del titular aparecen redactados por privacidad. Se anotaron las fechas de creación, actualización y expiración, junto con los estados del dominio y la información DNSSEC publicada.

### 2. DNS
Las consultas para `claude.ai` devolvieron:

- **A:** `160.79.104.10`
- **AAAA:** `2607:6bc0::10`
- **NS:** `isla.ns.cloudflare.com` y `randy.ns.cloudflare.com`
- **MX:** no se devolvieron registros MX en la consulta realizada.
- **TXT:** seis registros, incluidos valores de verificación de Google y `v=spf1 -all`.
- **CAA:** 18 registros en la respuesta observada.

Estos datos son una instantánea de las respuestas DNS y pueden cambiar.

### 3. Subdominios
La consulta de certificados públicos de `crt.sh` mostró, entre otros, `api.anthropic.com`, `api-staging.anthropic.com`, `console.anthropic.com`, `docs.anthropic.com`, `support.anthropic.com` y `status.anthropic.com`.

La aparición de un nombre en certificados no demuestra que el host esté activo ni que esté autorizado para pruebas.

### 4. Huella tecnológica
Netcraft reportó tecnologías y proveedores asociados a `anthropic.com`, incluidos Cloudflare, Google HTTPS Load Balancer, JavaScript y React Server Components. El informe también mostró información de SPF y una política DMARC `p=reject`.

Las identificaciones de tecnologías proporcionadas por terceros pueden ser incompletas o variar con el tiempo.

### 5. Ficheros públicos
- **`robots.txt`:** se observó `Allow: /` y una referencia al sitemap `https://www.anthropic.com/sitemap.xml`.
- **`security.txt`:** publicó un contacto de HackerOne, una política de divulgación responsable, el idioma preferido inglés y una expiración declarada para el 31 de diciembre de 2026.

Estos archivos aportan información pública, pero por sí mismos no demuestran una vulnerabilidad.

### 6. Servicios listados públicamente
Shodan InternetDB asoció la IP `160.79.104.10` con los nombres `claude.anthropic.com` y `a.anthropic.com`, y reportó Cloudflare como CPE.

La fuente enumeró los puertos 80, 443, 2052, 2082, 2083, 2086, 2087, 2096, 8080, 8443 y 8880, sin vulnerabilidades listadas en esa respuesta. No se verificó el estado actual de esos puertos mediante escaneo.

### 7. Google dorks
La búsqueda `site:anthropic.com filetype:pdf` mostró documentos públicos indexados, incluidos informes corporativos, publicaciones de investigación y documentos relacionados con seguridad de IA.

La indexación en buscadores no demuestra que los documentos estén expuestos indebidamente.

### 8. Correos y metadatos
La ejecución de `theHarvester -d anthropic.com -b crtsh` no devolvió IPs, correos, personas ni hosts en esa consulta. Esto solo describe el resultado de la fuente utilizada; no demuestra que no existan otros datos públicos.

## Evaluación general
Se completó una primera pasada por las ocho técnicas obligatorias de reconocimiento pasivo, documentando los resultados y las limitaciones de las fuentes consultadas.

Hasta este punto no se ha confirmado ninguna vulnerabilidad. Los datos obtenidos sirven como inventario preliminar y deben contrastarse con el alcance vigente antes de considerar cualquier prueba adicional.

La comparación con el agente de IA queda pendiente hasta disponer de sus resultados. Las diferencias deberán registrarse en `comparativa.md`, indicando la fuente y evitando considerar un hallazgo confirmado sin evidencia reproducible.