

# Informe de Reconocimiento Pasivo: claude.ai

---

## 1. Registro del Dominio (WHOIS)

| Campo | Valor | Fuente |
|---|---|---|
| **Dominio** | claude.ai | `whois_dominio` |
| **Fecha de registro** | 2018-08-04 | `whois_dominio` |
| **Fecha de expiración** | 2029-08-04 | `whois_dominio` |
| **Última transferencia** | 2023-11-28 | `whois_dominio` |
| **Last changed** | 2026-08-12 | `whois_dominio` |
| **Nameservers** | `isla.ns.cloudflare.com`, `randy.ns.cloudflare.com` | `whois_dominio` |
| **Estado** | client delete prohibited, client transfer prohibited, client update prohibited | `whois_dominio` |
| **Entidad registrant** | 3c75800c8cc9471ea43e70fe86c91bad-DONUTS | `whois_dominio` |

---

## 2. Registros DNS

### A / AAAA
- **A**: `160.79.104.10` (`dns_registros`)
- **AAAA**: `2607:6bc0::10` (`dns_registros`)

### NS
- `randy.ns.cloudflare.com.` (`dns_registros`)
- `isla.ns.cloudflare.com.` (`dns_registros`)

### MX
- Sin registros MX para `claude.ai`. (`dns_registros`)

### TXT
- `"google-site-verification=NISbSmcIQumvbPjLbYAhRmzrx1LSAhRMH6XVaKTWxe0"` (`dns_registros`)
- `"google-site-verification=iDyYpE6uHVggWrWzK-MEosRSp7XUE7wqBLGX0Ua71Pc"` (`dns_registros`)
- `"v=spf1 -all"` (`dns_registros`)
- `"_4h91g65hky8g6rbfx22rpfu4pprn1v3"` (`dns_registros`)
- `"google-site-verification=vd3zHrSm-qrk36v4haRXBGrfAOM-O8b8pDiaPdI_s9Q"` (`dns_registros`)
- `"google-site-verification=YPYhXirYOvYGGQtAypqom1k-1KMXKHeWbxKgw60bDfo"` (`dns_registros`)

**Nota**: El SPF `"v=spf1 -all"` indica que **no se autoriza el envío de correo desde ningún servidor** para `claude.ai`, consistente con la ausencia de registros MX.

### CNAME
- Sin registros CNAME. (`dns_registros`)

### SOA
- `isla.ns.cloudflare.com. dns.cloudflare.com. 2419399531 10000 2400 604800 1800` (`dns_registros`)

### CAA
Múltiples emisores autorizados para certificados: (`dns_registros`)
- `0 issue "comodoca.com"`
- `0 issuewild "comodoca.com"`
- `0 issue "amazon.com"`
- `0 issuewild "amazon.com"`
- `0 issue "amazonaws.com"`
- `0 issuewild "amazonaws.com"`
- `0 issue "pki.goog; cansignhttpexchanges=yes"`
- `0 issuewild "pki.goog; cansignhttpexchanges=yes"`
- `0 issue "amazontrust.com"`
- `0 issuewild "amazontrust.com"`
- `0 issuewild "ssl.com"`
- `0 issuewild "digicert.com; cansignhttpexchanges=yes"`
- `0 issue "digicert.com; cansignhttpexchanges=yes"`
- `0 issue "awstrust.com"`
- `0 issuewild "awstrust.com"`
- `0 issue "letsencrypt.org"`
- `0 issuewild "letsencrypt.org"`
- `0 issue "ssl.com"`

**Nota**: Soporta tanto emisiones estándar como con `cansignhttpexchanges=yes` (para TLS Certificate Transparency/HTTP Exchanges), con un amplio set de CA incluyendo Let's Encrypt, Amazon, Google, DigiCert y Comodo.

---

## 3. Subdominios

- **No disponibles**: `crt.sh` respondió con error HTTP 502 en tres intentos consecutivos. No se pudieron enumerar subdominios por transparencia de certificados. (`subdominios_crtsh`)
- **theHarvester** no encontró hosts asociados a `claude.ai`. (`correos_theharvester`)

---

## 4. robots.txt

Contenido de `https://claude.ai/robots.txt`: (`robots_txt`)

```
User-Agent: ia_archiver
Allow: /$
Allow: /login
Disallow: /

User-Agent: GPTBot
User-Agent: OAI-SearchBot
User-Agent: ChatGPT-User
User-Agent: Google-Extended
Disallow: /

User-Agent: *
Allow: /api/desktop/
Disallow: /api/*
Disallow: /lti/*

Sitemap: https://claude.ai/sitemap.xml
```

**Hallazgos clave**:
- **Bloqueo activo de bots de IA**: GPTBot (OpenAI), ChatGPT-User, OAI-SearchBot y Google-Extended tienen acceso completamente denegado (`Disallow: /`).
- Wayback Machine (`ia_archiver`) solo puede indexar la raíz `/` y `/login`.
- Los crawlers generales (`*`) tienen acceso a `/api/desktop/` pero están excluidos de `/api/*` y `/lti/*`.
- Se anuncia un sitemap en `https://claude.ai/sitemap.xml`.

---

## 5. security.txt

La consulta a `/.well-known/security.txt` devolvió **HTML de la página principal de Claude** (un documento React con ~150 KB) en lugar de un archivo `security.txt` conforme al RFC 9116. (`security_txt`)

**Interpretación**: No se detectó un `security.txt` válido en `claude.ai`. El servidor responde con la landing page tanto en la raíz como en `/.well-known/security.txt`.

---

## 6. Correos (theHarvester)

- No se encontraron emails, IPs, personas ni hosts asociados a `claude.ai` vía crt.sh. (`correos_theharvester`)

---

## 7. Objetivos Fuera de Alcance

Los siguientes objetivos solicitados fueron **BLOQUEADOS** por encontrarse fuera del alcance autorizado:

| Objetivo | Herramienta | Estado |
|---|---|---|
| `anthropic.com` (WHOIS) | `whois_dominio` | ❌ BLOQUEADO |
| `www.anthropic.com` (robots.txt) | `robots_txt` | ❌ BLOQUEADO |
| `160.79.104.10` (Shodan) | `shodan_internetdb` | ❌ BLOQUEADO |

**Nota**: La IP `160.79.104.10` es exactamente la dirección IPv4 que resuelve `claude.ai` (registro A), pero como objetivo de Shodan está fuera del scope autorizado y no se pudieron consultar sus datos de puertos, servicios y CVEs.

---

## 8. Resumen Ejecutivo

`claude.ai` es un dominio registrado desde 2018, resuelto por Cloudflare (`160.79.104.10` / `2607:6bc0::10`) con un amplio conjunto de CA autorizadas en sus registros CAA. El dominio no opera correo propio (SPF `-all`, sin MX). Su `robots.txt` revela una política activa de **exclusión de bots de inteligencia artificial** (GPTBot, ChatGPT-User, OAI-SearchBot), sugiriendo una estrategia deliberada de control de contenido para entrenamiento de modelos de terceros. No se detectó un `security.txt` válido ni se pudo obtener información de Shodan para la IP asociada por restricciones de alcance.