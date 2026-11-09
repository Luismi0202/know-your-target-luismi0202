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

---

## Dónde está cada parte

### Parte 1 · Mapa de superficie de ataque

| Apartado del enunciado | Dónde está |
|---|---|
| 1.1 Elige tu objetivo | Este README (*Objetivo elegido*) y [`alcance.md`](alcance.md), sección 1 |
| 1.2 Lee las reglas y escribe tu alcance | [`alcance.md`](alcance.md) y [`scope.txt`](scope.txt) |
| 1.3 Reconocimiento pasivo: las ocho técnicas obligatorias | [`cuaderno.md`](cuaderno.md), registros 2 a 15 |
| 1.3 Reconocimiento pasivo: técnicas opcionales | [`cuaderno.md`](cuaderno.md), registros 16 a 22 y *Resumen de técnicas opcionales* |
| 1.4 Cuaderno de trabajo | [`cuaderno.md`](cuaderno.md) |
| 1.5 El mapa | [`mapa.md`](mapa.md) |

### Parte 2 · First Agent

| Apartado del enunciado | Dónde está |
|---|---|
| 2.1 Comprueba tu alcance (`scope.txt`) | [`agente/pruebas.md`](agente/pruebas.md), secciones 0 y 2.1 |
| 2.2 Dale herramientas | [`agente/pruebas.md`](agente/pruebas.md), sección 2.2, y el código en [`agente/src/`](agente/src/) |
| 2.3 Mira cómo se construye su prompt | [`agente/pruebas.md`](agente/pruebas.md), sección 2.3, y la plantilla en [`agente/instrucciones.md`](agente/instrucciones.md) |
| 2.4 Lánzalo contra tu objetivo | [`agente/pruebas.md`](agente/pruebas.md), sección 2.4; [`agente/traza.jsonl`](agente/traza.jsonl), [`agente/traza.log`](agente/traza.log) e [`agente/informe.md`](agente/informe.md) |
| 2.5 Intenta sacarlo del alcance | [`agente/pruebas.md`](agente/pruebas.md), sección 2.5; [`traza_fuera_1.jsonl`](agente/traza_fuera_1.jsonl) / [`informe_fuera_1.md`](agente/informe_fuera_1.md) y [`traza_fuera_2.jsonl`](agente/traza_fuera_2.jsonl) / [`informe_fuera_2.md`](agente/informe_fuera_2.md) |

### Parte 3 · Análisis comparativo

| Apartado del enunciado | Dónde está |
|---|---|
| 3.1 La comparación | [`comparativa.md`](comparativa.md), sección 3.1 (tabla por dato y resumen con números) |
| 3.2 Los fallos del agente | [`comparativa.md`](comparativa.md), sección 3.2 (omisiones, errores, invenciones e intentos fuera de alcance) |
| 3.3 Reflexión | [`comparativa.md`](comparativa.md), sección 3.3 |

### Estructura del repositorio

```text
know-your-target-luismi0202/
├── README.md              # este documento
├── alcance.md             # programa, reglas y alcance
├── scope.txt              # alcance (el mismo en la Parte 1 y la Parte 2)
├── cuaderno.md            # cuaderno de trabajo de la Parte 1
├── mapa.md                # mapa de superficie de ataque
├── comparativa.md         # Parte 3
├── IMGS/                  # capturas (las de la Parte 2 empiezan por p2_)
└── agente/
    ├── src/               # tus_herramientas.py, lanzar.py y test_recon.py
    ├── pruebas.md         # Parte 2: scope-guard, herramientas, prompt, ejecución e intentos
    ├── instrucciones.md   # plantilla del prompt
    ├── traza.jsonl        # ejecución completa contra Anthropic (+ traza.log legible)
    ├── informe.md         # informe que generó el agente
    └── traza_fuera_*.jsonl / informe_fuera_*.md   # intentos de sacarlo del alcance
```

---

## Resumen del trabajo

### Parte 1 · Mapa de superficie de ataque

Apliqué las ocho técnicas obligatorias, solo de forma pasiva:

- WHOIS, con ICANN Lookup, porque `whois` no funcionaba desde el Kali.
- DNS con `dig`: A, AAAA, MX, NS, TXT y CAA.
- Subdominios con crt.sh.
- Netcraft.
- `robots.txt` y `security.txt`.
- Shodan InternetDB.
- Google dorks.
- theHarvester.

Después añadí técnicas opcionales:

- DNS y RDAP de `api.anthropic.com`.
- Wayback Machine.
- Una prueba de ExifTool.
- LinkedIn.
- Have I Been Pwned.
- Sherlock.

Cada consulta está en el cuaderno con su fecha, objetivo, comando, resultado y siguiente paso.

Lo más relevante:

- `claude.ai` usa DNS de Cloudflare, resuelve a `160.79.104.10` / `2607:6bc0::10`, no tiene MX y publica `v=spf1 -all`.
- crt.sh muestra muchos subdominios de `anthropic.com`. Los clasifiqué contra mi alcance, y nombres como `status.` o `www.` quedan fuera.
- Shodan asocia la IP de `claude.ai` a 11 puertos y a nombres que no están en mi alcance.
- Según ARIN, los bloques de IP consultados están registrados a nombre de Anthropic, PBC.
- No encontré ningún correo ni un patrón de correo con theHarvester.

### Parte 2 · First Agent

Usé `aap-base` en el Kali del aula con mi mismo `scope.txt`. A las tres herramientas de partida (`whois_dominio`, `dns_registros`, `subdominios_crtsh`) les añadí cuatro más, todas protegidas por el scope-guard: `robots_txt`, `security_txt`, `shodan_internetdb` y `correos_theharvester`. También añadí el tipo `CAA` en `dns_registros`.

- **Scope-guard:** pasan los 44 tests del proyecto y los 12 casos de mi batería. Todas las herramientas devuelven `BLOQUEADO` fuera del alcance.
- **Ejecución:** modelo `corsario-1`, 7 minutos, 6 pasos y 53 llamadas a herramientas, con 34 558 tokens de entrada y 6 886 de salida.
- **Bloqueos:** el guard paró las 14 llamadas fuera de alcance de las tres ejecuciones (otra empresa, subdominio excluido, dominio raíz, URL e IP).

### Parte 3 · Comparativa

El agente fue más rápido y más sistemático: resolvió el DNS de todos los hosts del alcance, cosa que yo no hice. Pero se quedó sin subdominios, tecnologías, dorks ni Shodan, por falta de herramientas o por las limitaciones de mi alcance. Además, añadió al informe suposiciones que ninguna herramienta le devolvió y no respetó el límite de llamadas del prompt. Por eso, el informe del agente hay que revisarlo siempre contra la traza.

## Reglas que he seguido

- Solo técnicas pasivas: sin escaneo de puertos, sin escáneres de vulnerabilidades y sin fuerza bruta.
- No he interactuado con personas ni he creado cuentas en servicios de Anthropic.
- No he encontrado datos sensibles. Si los hubiera encontrado, los habría anotado sin el dato y habría avisado al profesor.
- Algunas consultas de la Parte 1 se hicieron sobre `anthropic.com`, que no está en el alcance, como consulta de fuentes públicas. Están identificadas así en el cuaderno y el mapa, y no se tratan como autorización.
- El agente usa la IA del aula. El `.env` con la clave no está en el repositorio.

---

## Estado frente a la rúbrica

| Apartado | Peso | Dónde está |
|---|---|---|
| Alcance (P1) | 10 % | Programa público y activo de HackerOne, con enlace y fecha de consulta, en [`alcance.md`](alcance.md) (secciones 1 y 2). Activos dentro y fuera, en la sección 3. Exclusiones y limitaciones, en la sección 4. Reglas del programa que afectan al proyecto, en la sección 6. El alcance traducido a [`scope.txt`](scope.txt), con los siete hosts autorizados y las exclusiones con `!`. |
| Reconocimiento pasivo (P1) | 20 % | Las ocho técnicas obligatorias, cada una interpretada, en [`cuaderno.md`](cuaderno.md) (registros 2 a 15). Las técnicas opcionales (DNS y RDAP, Wayback Machine, ExifTool, LinkedIn, Have I Been Pwned y Sherlock) en los registros 16 a 22. El contraste entre fuentes, en la sección *Contraste entre fuentes* del cuaderno y en [`mapa.md`](mapa.md) (sección 2). Las capturas, en [`IMGS/`](IMGS/). |
| Mapa de superficie (P1) | 15 % | [`mapa.md`](mapa.md): resumen (1), tabla de hosts con IP, alcance y uso (2), infraestructura y servicios (3), correos y personas (4), y tres puntos de interés justificados (5). Cada dato remite a su registro del cuaderno. |
| Cuaderno de trabajo (P1) | 10 % | [`cuaderno.md`](cuaderno.md): cada registro tiene fecha, objetivo y estado de alcance, comando o acción, resultado, siguiente paso, y la captura correspondiente. |
| scope-guard (P2) | 15 % | En [`agente/pruebas.md`](agente/pruebas.md): los tests (sección 0), la batería con 12 casos propios de Anthropic (2.1), las siete herramientas protegidas con `@protegida` y probadas a mano dentro y fuera del alcance (2.2), y los bloqueos del agente con su trozo de traza (2.4 y 2.5). Capturas `p2_*` en [`IMGS/`](IMGS/). |
| Agente en marcha (P2) | 10 % | Las cuatro herramientas nuevas, más `CAA`, en [`agente/src/tus_herramientas.py`](agente/src/tus_herramientas.py), activas en [`agente/src/lanzar.py`](agente/src/lanzar.py). Las instrucciones, con sus límites y la fuente de cada dato, en [`agente/instrucciones.md`](agente/instrucciones.md), analizadas en [`agente/pruebas.md`](agente/pruebas.md) (2.3). La traza en [`agente/traza.jsonl`](agente/traza.jsonl) y [`traza.log`](agente/traza.log), el informe en [`agente/informe.md`](agente/informe.md), y los tokens, el tiempo y el gasto en [`agente/pruebas.md`](agente/pruebas.md) (2.3 y 2.4). |
| Análisis comparativo (P3) | 20 % | [`comparativa.md`](comparativa.md): tabla dato por dato y resumen con números (3.1); fallos clasificados en omisión, error, invención e intento fuera de alcance, con ejemplos de la traza (3.2); y reflexión con ejemplos concretos (3.3). |
