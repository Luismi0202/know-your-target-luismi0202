# Alcance del proyecto — Know Your Target

## 1. Información del programa

- **Organización:** Anthropic
- **Plataforma:** HackerOne
- **Programa:** Anthropic Bug Bounty
- **URL:** https://hackerone.com/anthropic
- **Fecha de consulta:** 28/10/2026
- **Última actualización de la política consultada:** 28/09/2026
- **Fuente de los activos:** CSV descargado desde HackerOne el 28/10/2026.

## 2. Objetivo

Realizar el inventario previo a una auditoría mediante las ocho técnicas de reconocimiento indicadas en el enunciado, documentando fuentes, resultados y limitaciones. Para la Parte 2 se usará la misma lista de activos en `scope.txt` como allowlist del `scope-guard`.

En esta práctica, "pasivo" significa que no se escanean puertos, no se ejecutan pruebas de vulnerabilidades, no se fuerza acceso ni se interactúa con empleados. Algunas consultas de información pública sí generan tráfico (por ejemplo, consultas DNS o peticiones GET a archivos públicos), se anotan como tales y no se confunden con una ausencia total de paquetes.

## 3. Activos incluidos

Según el CSV descargado de HackerOne, los activos relevantes para el reconocimiento basado en dominios incluyen:

- claude.ai — Core
- api.anthropic.com — Core
- console.anthropic.com — Core
- docs.anthropic.com — Non-Core
- support.anthropic.com — Non-Core
- anthropic.atlassian.com — Non-Core

El activo API & SDKs también menciona expresamente api-staging.anthropic.com como hostname de staging. Se documentará por separado, respetando las instrucciones específicas del programa.

El programa incluye además otras categorías, como clientes oficiales, Claude Code, repositorios y servicios internos. No se tratarán como dominios sin comprobar primero su naturaleza y sus instrucciones específicas.

La allowlist incluye exactamente los siete nombres enumerados en `scope.txt`, sin comodines. Esto evita interpretar que cualquier subdominio relacionado queda permitido. `anthropic.com` y nombres descubiertos como `status.anthropic.com` no se añadieron porque no están confirmados en la lista de activos recogida aquí. Consultar una fuente pública que los menciona no cambia esa decisión.

## 4. Exclusiones y limitaciones

- El repositorio https://github.com/modelcontextprotocol aparece como no elegible para envíos ni recompensas en este programa. Sus problemas deben comunicarse a los mantenedores correspondientes.
- Los activos de terceros no quedan autorizados automáticamente por aparecer relacionados con Anthropic.
- Los problemas de seguridad del contenido o las respuestas de los modelos, incluidos los jailbreaks, están fuera de este programa de infraestructura.
- No se realizarán escaneos de puertos, fuerza bruta, explotación, pruebas de denegación de servicio ni ingeniería social.
- No se crearán cuentas en los sistemas objetivo ni se accederá, descargará o conservará información privada.
- Cualquier hallazgo sensible se documentará sin copiar datos sensibles y se comunicará al profesor.

## 5. Técnicas permitidas en esta práctica

Se utilizarán únicamente técnicas de reconocimiento pasivo y fuentes públicas, como:

- Consultas WHOIS.
- Consulta de registros DNS públicos.
- Revisión de fuentes públicas de subdominios.
- Consulta de información pública sobre tecnologías.
- Revisión pública de robots.txt y security.txt.
- Consulta de fuentes públicas como Shodan InternetDB.
- Búsquedas públicas con operadores de Google.
- Búsqueda de información de contacto publicada públicamente, minimizando los datos personales recopilados.

## 6. Reglas relevantes del programa

La política solicita informes detallados y reproducibles. Prohíbe causar daños, comprometer cuentas ajenas, realizar ingeniería social y acceder, extraer o conservar datos de otros usuarios.

Las pruebas deben mantenerse dentro de las condiciones del programa y de la legislación aplicable. La etiqueta «Open Scope» no sustituye la revisión de las instrucciones de cada activo.

En las notas consultadas para este trabajo no quedó registrado un límite numérico de peticiones, una autorización explícita para escaneo automatizado ni un requisito concreto de identificación del investigador. No se debe interpretar esa falta de anotación como permiso: la práctica no hará escaneos, y antes de cualquier actividad posterior habría que volver a comprobar la política y las instrucciones específicas. Esta práctica no contactará con empleados ni creará cuentas.

## 7. Registro de fuentes

- Programa: https://hackerone.com/anthropic
- Política y directrices del programa: sección Program guidelines de HackerOne.
- Alcance de activos: sección Scope y CSV descargado el 28/10/2026.

## 8. Uso de `scope.txt` y comprobación del scope-guard

`scope.txt` contiene una línea por hostname permitido, sin comodines ni rangos IP. Se usará el mismo archivo en las dos partes del proyecto. La inclusión de un nombre solo lo incorpora a la allowlist del agente, no autoriza técnicas prohibidas por la práctica ni prevalece sobre las condiciones del programa.

Al probar el `scope-guard` de `aap-base`, los casos esperados para esta lista son:

| Objetivo de prueba | Resultado esperado | Motivo |
|---|---|---|
| `api.anthropic.com` | Dentro | Coincidencia exacta con una línea de `scope.txt`. |
| `https://API.anthropic.com/login` | Dentro, si el guard normaliza mayúsculas y extrae el hostname de la URL | Es el mismo hostname autorizado, aunque tenga esquema, ruta y mayúsculas. |
| `status.anthropic.com` | Fuera | Se encontró en fuentes públicas, pero no está en la allowlist. |
| `anthropic.com` | Fuera | El dominio raíz no está enumerado. |
| `anthropic.com.evil.net` | Fuera | No coincide con ningún hostname autorizado, compartir texto no basta. |
| `anthropic.atlassian.com` | Dentro | Solo está incluido ese hostname exacto, no todo Atlassian. |
| `10.10.0.7` | Fuera | No se incluyeron direcciones IP ni rangos. |

La comprobación debe hacerse contra el `scope-guard` ya proporcionado por `aap-base`, no se programa otro guard. Se deben guardar en la traza los objetivos probados y el resultado permitido/rechazado. En este repositorio solo se documenta la lista, la ejecución del agente y esas pruebas quedan pendientes.

## 9. Estado

El alcance está normalizado en `scope.txt` y se ha documentado el reconocimiento manual en `cuaderno.md` y `mapa.md`. Queda pendiente ejecutar `aap-base` con esta misma lista, comprobar los casos del scope-guard y completar la comparativa con resultados reales del agente.