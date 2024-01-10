import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/", // Repo name (if not custom domain)
  plugins: [svelte()],
});
