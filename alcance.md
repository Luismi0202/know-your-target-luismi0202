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

Realizar reconocimiento pasivo de los activos autorizados de Anthropic para identificar y documentar información pública sobre sus dominios, infraestructura y tecnologías, sin explotar vulnerabilidades ni afectar los sistemas.

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

## 7. Registro de fuentes

- Programa: https://hackerone.com/anthropic
- Política y directrices del programa: sección Program guidelines de HackerOne.
- Alcance de activos: sección Scope y CSV descargado el 28/10/2026.

## 8. Estado

Alcance inicial documentado. Pendiente de completar el inventario de activos y registrar los resultados del reconocimiento pasivo en cuaderno.md y mapa.md.