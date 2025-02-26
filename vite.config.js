import path from "node:path";
import { defineConfig } from "vite";
import { globSync } from "glob";
import commonjs from '@rollup/plugin-commonjs';

export default defineConfig({
  server: {
    cors: true
  },
  root: __dirname,
  build: {
    outDir: path.join(__dirname, "./dist/"),
    manifest: "manifest.json",
    assetsDir: "bundled",
    // commonjsOptions: { transformMixedEsModules: true },
    rollupOptions: {
      input: [
        "src/static/main.js",
        "src/static/style.css",
        ...globSync("src/helpers/{javascript,css}/**/*.{css,js}")
      ],
      // output: {
      //   format: 'cjs'
      // }
    },
    emptyOutDir: true,
    copyPublicDir: false,
    // plugins: [commonjs()],
  },
});