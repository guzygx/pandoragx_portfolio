import path from "node:path";
import { defineConfig } from "vite";
import { globSync } from "glob";
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  server: {
    cors: true
  },
  root: __dirname,
  build: {
    outDir: path.join(__dirname, "./app/static/dist/"),
    manifest: "manifest.json",
    assetsDir: "bundled",
    rollupOptions: {
      input: [
        ...globSync("app/static/_css/prebuild/**/*.css"),
        ...globSync("app/static/_javascript/**/*.js")
      ],
    },
    emptyOutDir: true,
    copyPublicDir: false,
    plugins: [
      tailwindcss(),
    ]
  },
});
