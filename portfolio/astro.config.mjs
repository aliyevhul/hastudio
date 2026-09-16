// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  // Free Cloudflare Pages URL for now; swap to https://hastudio.az once the
  // domain is registered and pointed at this project.
  site: 'https://hastudio.pages.dev',
  vite: { plugins: [tailwindcss()] },
});
