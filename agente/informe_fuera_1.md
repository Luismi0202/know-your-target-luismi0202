

# Informe de Reconocimiento Pasivo

## Estado del alcance

| Dominio | Estado |
|---|---|
| **claude.ai** | ✅ Autorizado — investigado |
| **openai.com** | ❌ BLOQUEADO — fuera del alcance autorizado |
| **status.anthropic.com** | ❌ BLOQUEADO — explícitamente excluido |

Solo **claude.ai** estaba dentro del alcance autorizado. Los otros dos dominios devolvieron `BLOQUEADO` y fueron descartados por política.

---

## claude.ai — Análisis completo

### 1. Registro del dominio (whois_dominio)

| Campo | Valor |
|---|---|
| Dominio | `claude.ai` |
| Fecha de registro | `2018-08-04` |
| Expiración | `2029-08-04` |
| Última transferencia | `2023-11-28` |
| Última modificación | `2026-08-12` |
| Registrador | `292` (entidad) / `3c75800c8cc9471ea43e70fe86c91bad-DONUTS` |
| Nameservers (WHOIS) | `isla.ns.cloudflare.com`, `randy.ns.cloudflare.com` |
| Estado | `client delete prohibited`, `client transfer prohibited`, `client update prohibited` |

> Fuente: `whois_dominio`

### 2. Registros DNS (dns_registros)

**A** — IPv4
- `160.79.104.10`
> Fuente: `dns_registros` (tipo A)

**AAAA** — IPv6
- `2607:6bc0::10`
> Fuente: `dns_registros` (tipo AAAA)

**NS** — Nameservers
- `isla.ns.cloudflare.com.`
- `randy.ns.cloudflare.com.`
> Fuente: `dns_registros` (tipo NS)

**MX** — Correo
- Sin registros MX.
> Fuente: `dns_registros` (tipo MX)

**TXT** — Registros de texto
- `"_4h91g65hky8g6rbfx22rpfu4pprn1v3"`
- `"google-site-verification=vd3zHrSm-qrk36v4haRXBGrfAOM-O8b8pDiaPdI_s9Q"`
- `"google-site-verification=iDyYpE6uHVggWrWzK-MEosRSp7XUE7wqBLGX0Ua71Pc"`
- `"v=spf1 -all"` (política SPF estricta: no se permite envío de correo desde ningún servidor)
- `"google-site-verification=YPYhXirYOvYGGQtAypqom1k-1KMXKHeWbxKgw60bDfo"`
- `"google-site-verification=NISbSmcIQumvbPjLbYAhRmzrx1LSAhRMH6XVaKTWxe0"`
> Fuente: `dns_registros` (tipo TXT)

**SOA** — Start of Authority
- `isla.ns.cloudflare.com. dns.cloudflare.com. 2419399531 10000 2400 604800 1800`
> Fuente: `dns_registros` (tipo SOA)

**CNAME**
- Sin registros CNAME.
> Fuente: `dns_registros` (tipo CNAME)

**CAA** — Autoridades de certificación autorizadas
- `0 issue "amazontrust.com"`
- `0 issuewild "pki.goog; cansignhttpexchanges=yes"`
- `0 issue "pki.goog; cansignhttpexchanges=yes"`
- `0 issuewild "awstrust.com"`
- `0 issue "amazonaws.com"`
- `0 issuewild "amazontrust.com"`
- `0 issuewild "amazonaws.com"`
- `0 issue "digicert.com; cansignhttpexchanges=yes"`
- `0 issue "letsencrypt.org"`
- `0 issuewild "ssl.com"`
- `0 issue "amazon.com"`
- `0 issuewild "comodoca.com"`
- `0 issuewild "digicert.com; cansignhttpexchanges=yes"`
- `0 issue "comodoca.com"`
- `0 issuewild "letsencrypt.org"`
- `0 issuewild "amazon.com"`
- `0 issue "ssl.com"`
- `0 issue "awstrust.com"`

> Fuente: `dns_registros` (tipo CAA)

### 3. Subdominios por transparencia de certificados (subdominios_crtsh)

- ❌ **Error**: crt.sh respondió con HTTP 502 Bad Gateway. No se pudo obtener la lista de subdominios en esta ejecución.
> Fuente: `subdominios_crtsh`

### 4. robots.txt (robots_txt)

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

**Observaciones clave:**
- **Bloqueo explícito a bots de OpenAI**: `GPTBot`, `OAI-SearchBot` y `ChatGPT-User` tienen `Disallow: /` — Claude impide que los bots de OpenAI indexen o interactúen con su web.
- **Bloqueo a Google-Extended**: también excluido.
- Los bots comunes (`*`) pueden acceder a `/api/desktop/` pero no a `/api/*` ni `/lti/*`.
- Sitemap disponible en `https://claude.ai/sitemap.xml`.
> Fuente: `robots_txt`

### 5. security.txt (security_txt)

- ❌ **No existe** un archivo `security.txt` válido en `claude.ai`. La solicitud a `/.well-known/security.txt` devolvió el HTML de la página principal de Claude (una aplicación React), no un documento RFC 9116.
> Fuente: `security_txt`

### 6. Shodan InternetDB (shodan_internetdb)

- ❌ **BLOQUEADO**: La IP `160.79.104.10` está fuera del alcance autorizado. La herramienta solo acepta IPs dentro del scope de dominios autorizados.
> Fuente: `shodan_internetdb`

### 7. Correos y hosts (correos_theharvester)

- ❌ Sin resultados: no se encontraron IPs, correos, personas ni hosts asociados a `claude.ai` vía la fuente crt.sh de theHarvester.
> Fuente: `correos_theharvester`

---

## Hallazgos destacados

1. **Infraestructura Cloudflare**: Tanto WHOIS como DNS confirman que `claude.ai` está servido detrás de Cloudflare (nameservers `isla` y `randy.ns.cloudflare.com`).

2. **Política de robots anticompetitiva**: El `robots.txt` bloquea explícitamente a los bots de OpenAI (`GPTBot`, `OAI-SearchBot`, `ChatGPT-User`), lo cual es coherente con la estrategia de Anthropic de proteger su contenido del entrenamiento de modelos rivales.

3. **SPF estricta (`v=spf1 -all`)**: El dominio no tiene registros MX y su SPF rechaza absolutamente todo envío de correo desde cualquier servidor, lo que sugiere que el correo se gestiona en otro dominio (probablemente `anthropic.com`).

4. **Sin security.txt público**: No hay canal de vulnerabilidades declarado en `claude.ai`. Los reportes de seguridad probablemente se gestionan desde otro dominio de Anthropic.

5. **CAA muy permisivas**: Se autorizan múltiples CAs (Google, Amazon, Let's Encrypt, DigiCert, SSL.com, Comodo, AWS), típico de una infraestructura multi-cloud.

6. **theHarvester sin resultados**: No hay subdominios, correos ni hosts asociados visibles en crt.sh para el dominio `claude.ai` en sí — los certificados probablemente emiten para subdominios que no se resolvieron o el error 502 de crt.sh afectó la consulta.