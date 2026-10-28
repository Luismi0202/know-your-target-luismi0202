# Mapa de superficie de ataque: Anthropic

- **Programa consultado:** Anthropic Bug Bounty, HackerOne
- **Política:** https://hackerone.com/anthropic
- **Fecha de consulta del alcance:** 28/10/2026
- **Fuentes y fecha de las observaciones:** las anotaciones del cuaderno, realizadas el 28/10/2026
- **Alcance operativo de este inventario:** los siete hostnames exactos de `scope.txt`; no se ha usado un comodín.

## 1. Resumen

Anthropic ofrece un programa público de bug bounty en HackerOne.
La allowlist de este trabajo contiene siete hostnames que se identificaron en la información del programa.
En `claude.ai` se observaron direcciones IPv4 e IPv6 y nameservers de Cloudflare.
Fuentes públicas reportaron también tecnologías web, documentos indexados y metadatos de servicios.
No se confirmó ninguna vulnerabilidad; los datos son una instantánea y los nombres descubiertos no amplían el alcance.

## 2. Dominios y subdominios

La columna "En alcance" indica si el hostname aparece literalmente en `scope.txt`; no confirma que esté activo ni autoriza pruebas distintas de las permitidas por el programa y esta práctica. Las direcciones IP solo se anotan cuando se consultaron expresamente; no se inventan resoluciones para el resto.

| Hostname | IP observada | En alcance según `scope.txt` | Uso aparente o motivo por el que aparece |
|---|---|---|---|
| `claude.ai` | `160.79.104.10`; `2607:6bc0::10` | Sí | Servicio web asociado a Claude; IP y DNS consultados directamente en fuentes DNS públicas. |
| `api.anthropic.com` | No resuelta en este trabajo | Sí | Host de API, incluido en los activos del programa y visto en certificados públicos. |
| `api-staging.anthropic.com` | No resuelta en este trabajo | Sí, hostname mencionado expresamente en el activo API & SDKs | Host de staging indicado por la información del programa y visto en certificados públicos. |
| `console.anthropic.com` | No resuelta en este trabajo | Sí | Consola; activo enumerado en el alcance y nombre visto en certificados. |
| `docs.anthropic.com` | No resuelta en este trabajo | Sí | Documentación; activo enumerado en el alcance y nombre visto en certificados. |
| `support.anthropic.com` | No resuelta en este trabajo | Sí | Soporte; activo enumerado en el alcance y nombre visto en certificados. |
| `anthropic.atlassian.com` | No resuelta en este trabajo | Sí, Non-Core según la fuente consultada | Host relacionado con Atlassian; se conserva como hostname exacto, sin extender el permiso a otros activos de Atlassian. |
| `status.anthropic.com` | No resuelta en este trabajo | No | Nombre que apareció en certificados; no se incluyó en la allowlist. |
| `www.anthropic.com` | No resuelta en este trabajo | No | Nombre que apareció en certificados; no se incluyó en la allowlist. |
| `www-cdn.anthropic.com` | No resuelta en este trabajo | No | Dominio mencionado en resultados de búsqueda; no se confirmó su relación con un activo autorizado. |
| `claude.anthropic.com` y `a.anthropic.com` | No resueltas por separado | No | Nombres asociados por Shodan a la IP consultada; no aparecen en `scope.txt`. |
| `anthropic.com` | No corresponde: no se resolvió aquí | No | Dominio usado como consulta en crt.sh, Netcraft, Google, theHarvester y para consultar archivos públicos. No está en la allowlist. |

**Importante:** crt.sh, Shodan y los buscadores son fuentes de datos, no validadores de autorización. Un nombre encontrado allí no se incorpora al alcance por ese motivo. `anthropic.com` tampoco se debe tratar como permitido solo por ser el dominio raíz de varios nombres enumerados.

La captura del registro 9 muestra más resultados de crt.sh que los ejemplos transcritos en el cuaderno. Por eso esta tabla clasifica todos los nombres que quedaron anotados en los documentos, pero no afirma ser el listado exhaustivo devuelto por crt.sh. Para entregar un inventario completo, hay que conservar y revisar la salida íntegra, deduplicar los nombres y marcar cada uno contra `scope.txt`.

## 3. Infraestructura y servicios

### DNS y registro

Para `claude.ai`, ICANN Lookup indicó Markmonitor Inc. como registrador y los nameservers `isla.ns.cloudflare.com` y `randy.ns.cloudflare.com`. Las consultas DNS devolvieron una IPv4, una IPv6, esos dos NS, seis TXT y 18 CAA. La consulta MX no devolvió registros. El TXT SPF observado fue `v=spf1 -all`. Son respuestas puntuales; la falta de MX en `claude.ai` no permite concluir que la organización no use correo. (Cuaderno, registros 2-8.)

### Tecnologías y entrega web

Netcraft reportó Cloudflare, Google HTTPS Load Balancer, SignalPoint Communications como hosting indicado y tecnologías como JavaScript y React Server Components para `anthropic.com`. También presentó información SPF y DMARC, con `p=reject`. Son identificaciones de un tercero sobre un dominio que no figura en `scope.txt`; no se verificaron directamente ni deben interpretarse como una configuración confirmada de cada hostname del alcance. (Cuaderno, registro 10.)

### Archivos públicos

La consulta de `robots.txt` mostró `Allow: /` y un enlace a un sitemap. `security.txt` publicó un contacto de HackerOne, una política de divulgación, el idioma inglés y una fecha de expiración declarada para el 31/12/2026. Ambos archivos se consultaron en `anthropic.com`, que no está en la allowlist. `robots.txt` no controla el acceso y ninguno de los dos archivos demuestra por sí mismo un fallo. (Cuaderno, registros 11-12.)

### Datos publicados por Shodan

InternetDB asoció la IP `160.79.104.10` con `claude.anthropic.com` y `a.anthropic.com`, identificó un CPE de Cloudflare y enumeró los puertos 80, 443, 2052, 2082, 2083, 2086, 2087, 2096, 8080, 8443 y 8880. No se conectó a esos puertos ni se comprobó su estado actual. La fuente no listó vulnerabilidades en la respuesta consultada. Los hostnames asociados tampoco están incluidos en `scope.txt`. (Cuaderno, registro 13.)

## 4. Correos y personas

No se recopilaron nombres de empleados ni direcciones personales. La ejecución de `theHarvester` con la fuente crt.sh no devolvió correos, personas ni hosts; crt.sh no es una fuente especializada en correos, por lo que este resultado no permite establecer que no existan emails públicos ni deducir un patrón corporativo. Netcraft mostró datos SPF/DMARC para `anthropic.com`, pero no se verificó un patrón de direcciones. (Cuaderno, registros 10 y 15.)

## 5. Tres puntos para priorizar si se autoriza una fase posterior

Estos son temas para revisar primero, no hallazgos ni instrucciones para probar sistemas. Cualquier actividad futura requeriría comprobar de nuevo las reglas y el alcance exacto.

1. **Confirmar la cobertura de cada hostname de API y staging.** Son activos relevantes y aparecen en el alcance consultado; antes de cualquier evaluación habría que revisar las instrucciones específicas de cada uno. Su aparición en crt.sh no confirma que estén activos. (Registros 1 y 9.)
2. **Aclarar el alcance de los nombres asociados a la IP de `claude.ai`.** Shodan relacionó esa IP con dos nombres que no figuran en `scope.txt`. La prioridad es resolver administrativamente si están cubiertos por el programa, no asumir que lo están ni contactarlos. (Registros 3 y 13.)
3. **Completar el inventario de correo y tecnologías con fuentes adecuadas y permitidas.** La consulta de theHarvester usó crt.sh y no identificó un patrón de correo; los datos de Netcraft son indicios de `anthropic.com`, que no está en la allowlist. Haría falta documentar fuentes autorizadas antes de extraer conclusiones adicionales. (Registros 10 y 15.)

## Limitaciones y conclusión

El mapa junta observaciones de DNS, registros, certificados y bases de datos públicas. Algunas consultas se hicieron sobre `anthropic.com`, que no aparece en `scope.txt`; quedan identificadas como consultas a fuentes públicas, no como autorización para probar ese dominio. En una repetición con el agente, el `scope-guard` debe permitir solo los hostnames exactos de la allowlist y rechazar los demás.

No se escanearon puertos, no se lanzó un escáner de vulnerabilidades, no se hizo fuerza bruta ni se intentó acceder a datos privados. No se confirmó ninguna vulnerabilidad.
