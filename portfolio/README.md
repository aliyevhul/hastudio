# Portfolio site

Astro + Tailwind v4. Two pages: `/` (Azerbaijani) and `/en/` (English).

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
```

## Where to edit

- **All copy and prices** → `src/i18n/content.ts`. One file, both languages.
  You should never need to open a component to change wording.
- **Your name, email, phone, WhatsApp** → the `site` object at the top of that file.
- **Colours and fonts** → `@theme` block in `src/styles/global.css`.
- **Sections** → `src/components/*.astro`, assembled in `src/pages/index.astro`.

## Before publishing — the TODO list

1. `site.brand` — your real name or brand.
2. `site.email`, `site.phone`, `site.phoneHref`, `site.whatsapp`.
3. **Prices in `services.packages`** — the current numbers are placeholders.
4. `work.items` — replace with real projects, delete the filler.
5. `site` in `astro.config.mjs` — your real domain.
6. The contact form currently opens the visitor's mail app. For real submissions,
   point it at Formspree / Web3Forms in `src/components/Contact.astro`.
