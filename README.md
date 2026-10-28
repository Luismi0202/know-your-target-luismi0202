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
Se preparó una allowlist de siete hostnames concretos identificados en la información del programa:

- `claude.ai`
- `api.anthropic.com`
- `api-staging.anthropic.com`
- `console.anthropic.com`
- `docs.anthropic.com`
- `support.anthropic.com`
- `anthropic.atlassian.com`

La lista se encuentra en `scope.txt` y es la misma que se debe usar en la Parte 2 con `aap-base`. No contiene comodines: que un subdominio aparezca en certificados, Shodan o Google no lo añade al alcance. La inclusión de un hostname tampoco permite saltarse las restricciones de la práctica o del programa.

Se identificó `https://github.com/modelcontextprotocol` como excluido según la información del programa consultada. Los servicios de terceros no se consideran automáticamente dentro del alcance. Las pruebas de seguridad de modelos, como jailbreaks, se encuentran fuera del programa de infraestructura descrito.

Durante el reconocimiento se usó `anthropic.com` como consulta en varias fuentes y se consultaron sus archivos públicos `robots.txt` y `security.txt`. Ese dominio no figura en `scope.txt`; estas observaciones se identifican como fuentes consultadas, no como permiso para probarlo. Para repetir el trabajo con el agente, no se debe añadir sin comprobar antes la política vigente.

## Comprobación prevista del scope-guard

El `scope-guard` ya viene implementado en `aap-base`; este proyecto no lo programa. Al ejecutar el agente, se debe comprobar que permite un hostname exacto como `api.anthropic.com` y rechaza `status.anthropic.com`, `anthropic.com` y `anthropic.com.evil.net`. También se debe comprobar que `anthropic.atlassian.com` no da permiso para otros hosts de Atlassian. La política y los resultados de esas pruebas se deben conservar en la traza del agente. La ejecución aún está pendiente.

## Metodología
Se realizó reconocimiento de fuentes públicas sin escanear puertos ni probar vulnerabilidades, sin intentar acceder a datos privados y sin contactar con personas. Algunas consultas DNS y peticiones GET a archivos públicos generan tráfico; por eso "pasivo" describe aquí el tipo de actividad, no que no se envíe ningún paquete.

Técnicas utilizadas:

1. **Registro de dominio:** consulta de ICANN Lookup para `claude.ai`, al no funcionar la consulta WHOIS desde la terminal.
2. **Registros DNS:** consultas `dig` para A, AAAA, NS, MX, TXT y CAA.
3. **Subdominios:** consulta de certificados públicos mediante `crt.sh` para `anthropic.com`.
4. **Huella tecnológica:** consulta del informe de Netcraft para `anthropic.com`.
5. **Ficheros públicos:** consulta de `robots.txt` y `security.txt`.
6. **Servicios expuestos en fuentes públicas:** consulta de Shodan InternetDB para la IP `160.79.104.10`, sin escanear puertos.
7. **Google dorks:** búsqueda de documentos PDF indexados mediante `site:anthropic.com filetype:pdf`.
8. **Correos y metadatos públicos:** ejecución de `theHarvester` usando la fuente `crtsh`. Esta fuente se basa en certificados y no es especializada en correos, por lo que la ausencia de resultados no demuestra que no existan direcciones públicas.

No se realizaron escaneos activos, fuerza bruta, explotación, ingeniería social ni intentos de acceso a información privada. No se crearon cuentas en los sistemas de la organización.

## Documentos
- `alcance.md`: reglas, restricciones y alcance normalizado.
- `scope.txt`: allowlist exacta de siete hostnames, sin comodines.
- `cuaderno.md`: registro de fechas, objetivos, acciones, resultados, siguientes pasos y una explicación sencilla de para qué sirvió cada consulta.
- `mapa.md`: resumen de la superficie de ataque observada mediante fuentes públicas.
- `comparativa.md`: comparación con el agente de IA, pendiente de completar cuando se disponga de sus resultados.

## Estado frente a la rúbrica

Este estado resume lo que está documentado en el repositorio; no sustituye una calificación ni presenta como ejecutadas tareas que siguen pendientes.

| Apartado | Evidencia actual | Pendiente para aspirar al nivel excelente |
|---|---|---|
| Alcance (P1) | Programa, activos, restricciones y una allowlist exacta están descritos en `alcance.md` y `scope.txt`. | Confirmar en la política vigente si el programa declara algún comodín. No añadirlo por cumplir la rúbrica si amplía el permiso; conservar exclusiones justificadas y documentar las reglas de automatización, límites y requisitos con evidencia de la política. |
| Reconocimiento pasivo (P1) | El cuaderno registra las ocho técnicas obligatorias e incluye una sección de contraste entre fuentes. | Conservar la salida íntegra de crt.sh para completar la lista de nombres; registrar una técnica opcional si se realiza y solo después de comprobar que es apropiada y permitida. |
| Mapa (P1) | El mapa contiene resumen, tabla de hosts, infraestructura, correo/personas y tres prioridades con referencias a registros. | Completar el inventario a partir de evidencia íntegra y mantener la trazabilidad de cada dato al cuaderno. |
| Cuaderno (P1) | Las entradas describen objetivo, alcance, acción, resultado, siguiente paso y una explicación sencilla; también guardan comandos y fuentes cuando constan. | La hora de los registros 9-15 no quedó en la evidencia original; las entradas lo indican en vez de inventar una hora. En futuras consultas, guardar fecha, hora y salida/captura desde el momento de ejecución. |
| Scope-guard (P2) | `alcance.md` enumera resultados esperados para casos positivos y negativos, inspirados en la batería del enunciado. | Ejecutar la batería de `aap-base`, comprobar que todas las herramientas pasan por el guard y adjuntar la traza real de permitidos y bloqueados. |
| Agente (P2) | El README describe los límites esperados, pero este repositorio no contiene la ejecución de `aap-base`. | Añadir y ejecutar al menos dos herramientas seguras, instrucciones que exijan fuente para cada dato y guardar traza, informe y coste real. |
| Comparativa (P3) | No hay resultados del agente para comparar todavía. | Crear `comparativa.md` después de la ejecución: contrastar manual y agente con ejemplos de la traza, clasificar aciertos, omisiones, errores e invenciones y razonar el impacto de cada diferencia. |

El enunciado y la rúbrica no justifican ampliar el alcance con `*.anthropic.com` sin evidencia de que ese comodín esté autorizado por el programa. Si la política publica un wildcard, se puede reflejar exactamente en `scope.txt` y mantener las exclusiones aplicables; si no, se conserva la allowlist concreta.

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

La ejecución de `aap-base`, las pruebas del `scope-guard` y la comparación con el agente de IA quedan pendientes. Cuando se realicen, las diferencias deberán registrarse en `comparativa.md`, indicando la fuente y evitando considerar un hallazgo confirmado sin evidencia reproducible.