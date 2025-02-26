import path from "node:path";
import { defineConfig } from "vite";
import { globSync } from "glob";

export default defineConfig({
  server: {
    cors: true
  },
  root: __dirname,
  build: {
    outDir: path.join(__dirname, "./dist/"),
    manifest: "manifest.json",
    assetsDir: "bundled",
    rollupOptions: {
      input: [
        ...globSync("src/{javascript,css}/**/*.{css,js}")
      ],
    },
    emptyOutDir: true,
    copyPublicDir: false,
  },
});
