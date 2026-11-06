

He completado todas las consultas posibles. Ahora genero el informe final.

---

# Informe de Reconocimiento Pasivo — Anthropic

**Fecha:** 2026-11-06  
**Alcance autorizado:** claude.ai, api.anthropic.com, api-staging.anthropic.com, console.anthropic.com, docs.anthropic.com, support.anthropic.com, anthropic.atlassian.com  
**Fuera de alcance:** anthropic.com, status.anthropic.com, www.anthropic.com, www-cdn.anthropic.com, claude.anthropic.com, a.anthropic.com

---

## 1. claude.ai

### Registro WHOIS
| Campo | Valor | Herramienta |
|---|---|---|
| Registración | 2018-08-04 | `whois_dominio` |
| Caducidad | 2029-08-04 | `whois_dominio` |
| Último cambio | 2026-08-12 | `whois_dominio` |
| Nameservers | isla.ns.cloudflare.com, randy.ns.cloudflare.com | `whois_dominio` / `dns_registros` |
| Estado | client delete/transfer/update prohibited | `whois_dominio` |

### DNS
| Tipo | Valor | Herramienta |
|---|---|---|
| A | `160.79.104.10` | `dns_registros` |
| AAAA | `2607:6bc0::10` | `dns_registros` |
| MX | Sin registros | `dns_registros` |
| NS | isla.ns.cloudflare.com, randy.ns.cloudflare.com | `dns_registros` |
| SOA | isla.ns.cloudflare.com / dns.cloudflare.com | `dns_registros` |
| TXT | `v=spf1 -all` (SPF restrictivo) | `dns_registros` |
| TXT | google-site-verification ×4 registros | `dns_registros` |
| TXT | `_4h91g65hky8g6rbfx22rpfu4pprn1v3` | `dns_registros` |
| CAA | Múltiples emisores: pki.goog, comodoca.com, digicert.com, ssl.com, amazon.com, letsencrypt.org, awstrust.com, amazontrust.com (algunos con `cansignhttpexchanges=yes`) | `dns_registros` |

### Subdominios (crt.sh)
- Solo `claude.ai` dentro del alcance (14 subdominios filtrados como fuera de alcance). `subdominios_crtsh`

### robots.txt
- **ia_archiver:** permite solo `/` y `/login`
- **GPTBot, OAI-SearchBot, ChatGPT-User, Google-Extended:** `Disallow: /` (bloqueado)
- **\* (resto):** permite `/api/desktop/`, bloquea `/api/*` y `/lti/*`
- Sitemap: `https://claude.ai/sitemap.xml`  
  → `robots_txt`

### security.txt
- No se encontró un security.txt válido (RFC 9116). La URL `https://claude.ai/security.txt` devuelve el HTML de la página principal. `security_txt`

### Correos (theHarvester)
- Sin correos ni hosts encontrados. `correos_theharvester`

---

## 2. api.anthropic.com

| Tipo | Valor | Herramienta |
|---|---|---|
| A | `160.79.104.10` | `dns_registros` |
| AAAA | `2607:6bc0::10` | `dns_registros` |
| MX | Sin registros | `dns_registros` |
| TXT | Sin registros | `dns_registros` |

### robots.txt
- No publicado (HTTP 404). `robots_txt`

### security.txt
- No publicado (HTTP 404 en ambas rutas `.well-known/` y raíz). `security_txt`

---

## 3. console.anthropic.com

| Tipo | Valor | Herramienta |
|---|---|---|
| A | `160.79.104.10` | `dns_registros` |
| AAAA | `2607:6bc0::10` | `dns_registros` |
| MX | Sin registros | `dns_registros` |
| TXT | `google-site-verification=zPypKKUlUod8yx5sCOO1IPgvZ0FUx1oOLT9MK-sNKqU` | `dns_registros` |

### robots.txt
- `Disallow: /api/`
- Sitemaps: `https://platform.claude.com/sitemap.xml`, `https://platform.claude.com/cookbook/sitemap.xml`  
  → `robots_txt`

### security.txt
- No publicado (HTTP 404). `security_txt`

---

## 4. docs.anthropic.com

| Tipo | Valor | Herramienta |
|---|---|---|
| A | `160.79.104.10` | `dns_registros` |
| AAAA | `2607:6bc0::10` | `dns_registros` |
| MX | Sin registros | `dns_registros` |
| TXT | Sin registros | `dns_registros` |

### robots.txt
- `Disallow: /api/`
- Sitemaps: `https://platform.claude.com/sitemap.xml`, `https://platform.claude.com/cookbook/sitemap.xml`  
  → `robots_txt`

### security.txt
- No se encontró un security.txt válido (RFC 9116). La URL devuelve HTML. `security_txt`

---

## 5. support.anthropic.com

| Tipo | Valor | Herramienta |
|---|---|---|
| A | `160.79.104.10` | `dns_registros` |
| AAAA | `2607:6bc0::10` | `dns_registros` |
| MX | Sin registros | `dns_registros` |
| TXT | Sin registros | `dns_registros` |

### robots.txt
- `Disallow: /not-authorized`, `/not-found`, `/[helpCenterIdentifier]/`
- `Crawl-delay: 1`
- Sitemap: `https://support.claude.com/sitemap.xml`  
  → `robots_txt`

### security.txt
- **Proveedor de seguridad: Intercom** (gestiona el help center de Anthropic)
- Contact: `https://bugcrowd.com/intercom`, `mailto:security@intercom.com`
- Policy: `https://www.bugcrowd.com/resource/standard-disclosure-terms/`
- Hiring: `https://intercom.com/careers`
- Expires: 2029-03-15  
  → `security_txt`

---

## 6. anthropic.atlassian.com

| Tipo | Valor | Herramienta |
|---|---|---|
| A | Sin registros | `dns_registros` |
| AAAA | Sin registros | `dns_registros` |
| CNAME | Sin registros | `dns_registros` |
| MX | Sin registros | `dns_registros` |
| TXT | Sin registros | `dns_registros` |

- **No se resuelve en DNS** — error al descargar robots.txt: `No address associated with hostname`
- security.txt: no disponible (mismo error de resolución)
- subdominios_crtsh: 0 subdominios en alcance

**Observación:** El host está en el alcance autorizado pero no tiene resolución DNS funcional actualmente. `dns_registros`, `robots_txt`, `security_txt`, `subdominios_crtsh`

---

## 7. api-staging.anthropic.com

- **BLOQUEADO** en todas las consultas. Confirmado como excluido del alcance.

---

## Resumen y hallazgos clave

### Infraestructura compartida
Todos los hosts de Anthropic (claude.ai, api.anthropic.com, console.anthropic.com, docs.anthropic.com, support.anthropic.com) resuelven a la **misma IP** (`160.79.104.10` / `2607:6bc0::10`), lo que indica un frontend unificado (probablemente Cloudflare + load balancer).

### DNS y correo
- Ningún host tiene registros MX → **no gestionan correo directamente**; usan servicios externos.
- claude.ai tiene SPF restrictivo (`v=spf1 -all`) → no envía correo desde ese dominio.

### Certificados (CAA)
claude.ai declara múltiples emisores autorizados incluyendo proveedores de HTTP Exchange Certificates (`.well-known` / `cansignhttpexchanges=yes`): pki.goog, digicert.com, amazon.com, amazontrust.com. `dns_registros`

### Robots y privacidad
- claude.ai bloquea activamente a **GPTBot, OAI-SearchBot y ChatGPT-User** → decisión explícita de no indexar contenido por IA de OpenAI/ChatGPT.
- console.anthropic.com y docs.anthropic.com comparten los mismos sitemaps de `platform.claude.com`.
- support.anthropic.com usa **Intercom** como plataforma de ayuda.

### security.txt (RFC 9116)
- **Ningún host** tiene un security.txt válido directamente. El de support.anthropic.com pertenece a Intercom.
- La ausencia de security.txt propio en claude.ai sugiere que la política de seguridad y reporte de vulnerabilidades podría estar documentada en otro canal (posiblemente en la web de Anthropic fuera de alcance).

### Shodan
- IP `160.79.104.10`: **fuera del alcance autorizado** para Shodan → no disponible. `shodan_internetdb`