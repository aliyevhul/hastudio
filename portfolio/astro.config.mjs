// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  // Hosted on Vercel at the domain root. When hastudio.az is registered and
  // pointed at this project, only `site` changes; `base` stays '/'.
  site: 'https://hastudio-seven.vercel.app',
  base: '/',
  vite: { plugins: [tailwindcss()] },
});
