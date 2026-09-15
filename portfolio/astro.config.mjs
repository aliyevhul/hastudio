// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  // TODO: set this to your real domain before deploying.
  site: 'https://example.az',
  vite: { plugins: [tailwindcss()] },
});
