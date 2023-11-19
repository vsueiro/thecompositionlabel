import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/fast-fashion-composition/", // Repo name
  plugins: [svelte()],
});
