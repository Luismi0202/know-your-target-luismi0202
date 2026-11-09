# Proyecto 1 · Know Your Target

## Objetivo elegido

| | |
|---|---|
| **Organización** | Anthropic |
| **Programa** | Anthropic Bug Bounty (programa público con recompensa) |
| **Plataforma** | HackerOne |
| **Política** | https://hackerone.com/anthropic |
| **Fecha de consulta** | 28/10/2026 |

Elegí Anthropic porque tiene un programa público y activo en HackerOne, con varios activos web (`claude.ai`, la API, la consola, la documentación y el soporte), y porque me interesaba ver la superficie de ataque de una empresa de IA.

El programa no publica un comodín del tipo `*.anthropic.com`, así que mi alcance es una **lista blanca de siete hostnames exactos**:

```text
claude.ai
api.anthropic.com
api-staging.anthropic.com
console.anthropic.com
docs.anthropic.com
support.anthropic.com
anthropic.atlassian.com
```

Excluyo expresamente (`!`) los nombres que encontré durante el reconocimiento pero que no están autorizados: `anthropic.com`, `status.anthropic.com`, `www.anthropic.com`, `www-cdn.anthropic.com`, `claude.anthropic.com` y `a.anthropic.com`. El detalle está en [`alcance.md`](alcance.md).

## Contenido del repositorio

| Parte | Documento | Qué contiene |
|---|---|---|
| Alcance | [`alcance.md`](alcance.md) | Programa, reglas que afectan al proyecto, qué está dentro y fuera, y casos de prueba del scope-guard. |
| Alcance | [`scope.txt`](scope.txt) | El alcance en formato de una línea por objetivo. Es el mismo en la Parte 1 y en la Parte 2. |
| Parte 1 | [`cuaderno.md`](cuaderno.md) | Cuaderno de trabajo: 15 registros con fecha, objetivo, comando, resultado y siguiente paso, más capturas. |
| Parte 1 | [`mapa.md`](mapa.md) | Mapa de superficie de ataque: resumen, tabla de hosts, infraestructura, correos y personas, y tres puntos de interés. |
| Parte 2 | [`agente/pruebas.md`](agente/pruebas.md) | Comprobación del scope-guard (2.1), herramientas (2.2), prompt (2.3), ejecución (2.4) e intentos de sacarlo del alcance (2.5). |
| Parte 2 | [`agente/src/`](agente/src/) | Mi código: `tus_herramientas.py` con las herramientas que añadí, `lanzar.py` con la lista `HERRAMIENTAS` y el test actualizado. |
| Parte 2 | [`agente/instrucciones.md`](agente/instrucciones.md) | La plantilla del prompt (sin modificar). |
| Parte 2 | [`agente/traza.jsonl`](agente/traza.jsonl) · [`traza.log`](agente/traza.log) | La ejecución completa del agente contra Anthropic. |
| Parte 2 | [`agente/informe.md`](agente/informe.md) | El informe que generó el agente. |
| Parte 2 | `agente/traza_fuera_1.jsonl` · `agente/traza_fuera_2.jsonl` | Las trazas de los dos intentos de sacarlo del alcance, con sus informes (`informe_fuera_1.md`, `informe_fuera_2.md`). |
| Parte 3 | [`comparativa.md`](comparativa.md) | Comparación entre mi reconocimiento y el del agente, clasificación de sus fallos y reflexión. |
| Capturas | [`IMGS/`](IMGS/) | Capturas de la Parte 1 y de la Parte 2 (las de la Parte 2 empiezan por `p2_`). |

## Resumen del trabajo

### Parte 1 · Mapa de superficie de ataque

Apliqué las ocho técnicas obligatorias, solo de forma pasiva: WHOIS (ICANN Lookup, porque `whois` no funcionaba desde el Kali), DNS con `dig` (A, AAAA, MX, NS, TXT, CAA), subdominios con crt.sh, Netcraft, `robots.txt` y `security.txt`, Shodan InternetDB, Google dorks y theHarvester.

Lo más relevante:

- `claude.ai` usa DNS de Cloudflare, resuelve a `160.79.104.10` / `2607:6bc0::10`, no tiene MX y publica `v=spf1 -all`.
- crt.sh muestra muchos subdominios de `anthropic.com`; los clasifiqué contra mi alcance, y nombres como `status.` o `www.` quedan fuera.
- Shodan asocia la IP de `claude.ai` a 11 puertos y a nombres que no están en mi alcance.
- No encontré ningún correo ni un patrón de correo con theHarvester.

### Parte 2 · First Agent

Usé `aap-base` en el Kali del aula con mi mismo `scope.txt`. A las tres herramientas de partida (`whois_dominio`, `dns_registros`, `subdominios_crtsh`) les añadí `robots_txt`, `security_txt`, `shodan_internetdb` y `correos_theharvester`, todas protegidas por el scope-guard, y el tipo `CAA` en `dns_registros`.

- **Scope-guard:** 12 de 12 casos salen como esperaba.
- **Ejecución:** modelo `corsario-1`, 7 minutos, 34 558 tokens de entrada y 6 886 de salida.
- **Intentos de sacarlo del alcance:** el guard bloqueó todos (otra empresa, subdominio excluido, dominio raíz, URL e IP) y el modelo no insistió por otro camino.

### Parte 3 · Comparativa

El agente fue más rápido y más sistemático: resolvió el DNS de todos los hosts del alcance, cosa que yo no hice. Pero se quedó sin subdominios, tecnologías, dorks ni Shodan, por falta de herramientas o por las limitaciones de mi alcance. Además, añadió al informe suposiciones que ninguna herramienta le devolvió. Por eso, el informe del agente hay que revisarlo siempre contra la traza.

## Reglas que he seguido

- Solo técnicas pasivas: sin escaneo de puertos, sin escáneres de vulnerabilidades y sin fuerza bruta.
- No he interactuado con personas ni he creado cuentas en servicios de Anthropic.
- No he encontrado datos sensibles; si los hubiera encontrado, los habría anotado sin el dato y habría avisado al profesor.
- Algunas consultas de la Parte 1 se hicieron sobre `anthropic.com`, que no está en el alcance, como consulta de fuentes públicas. Están identificadas así en el cuaderno y el mapa, y no se tratan como autorización.
- El `.env` con la clave de la IA no está en el repositorio.
