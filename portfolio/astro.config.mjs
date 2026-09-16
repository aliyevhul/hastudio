// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  // Free GitHub Pages hosting for now. When hastudio.az is registered and
  // pointed here, change these two lines to:
  //   site: 'https://hastudio.az',  base: '/'
  // Every internal link is built from BASE_URL, so nothing else needs touching.
  site: 'https://aliyevhul.github.io',
  base: '/hastudio',
  vite: { plugins: [tailwindcss()] },
});
