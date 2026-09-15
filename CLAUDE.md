# Working in this repo

This is the user's **freelance / portfolio** workspace. It is deliberately separate
from the HRMS/AIMP work. Do not mix the two.

## What this repo is for

1. The user's own portfolio site and case studies.
2. Websites built for paying clients.
3. Ideas, pricing, and lead tracking for the above.

## How to help here

- New idea from the user → append it to `IDEAS.md` under **Inbox** using the
  template there. Promote to **Shortlist** only when the user says it's worth doing.
- New client/site → create `sites/<client-slug>/` and start with `SCOPE.md`
  (what's in, what's out, price, deadline, who supplies content) before building.
- Push back on scope creep and on unpriced work. Say what something will cost in time.
- Prefer the smallest shippable version. A live ugly site beats a perfect local one.
- Anything built a second time → extract it into `assets/` and say so.

## Hard rules

- **Never commit secrets** — API keys, client passwords, `.env`, DB URLs.
  If the user pastes one, tell them and keep it out of the repo.
- Never publish or deploy anything client-facing without the user saying go.
- Client names and details are private; don't send them to external services.

## Portfolio site

`portfolio/` is Huseyn Aliyev's own site (Astro + Tailwind, AZ at `/`, EN at `/en/`).
All copy and pricing lives in `src/i18n/content.ts` — change wording there, never in
the components. The dark theme with the lime accent is the approved default; don't
replace the palette or add a light mode unless asked.

## Stack defaults (unless the user says otherwise)

- Static/marketing sites: plain HTML + CSS, or Astro when it needs content collections.
- App-ish sites: Next.js + Tailwind.
- Deploy: whatever is free and fast for the client's needs; state the cost before choosing.
