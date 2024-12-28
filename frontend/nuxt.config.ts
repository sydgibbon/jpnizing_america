export default defineNuxtConfig({
  devtools: { enabled: false },
  typescript: {
    typeCheck: true,
  },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  $production: {
    routeRules: {
      "/**": { ssr: true },
    },
  },

  $development: {
    //
  },

  runtimeConfig: {
    public: {
      MOODLE_URL: process.env.MOODLE_URL || 'http://localhost:80',
    },
  },

  compatibilityDate: "2024-09-29",

  webpack: {
    loaders: {
      vue: {
        hotReload: true,
      },
    },
  },

  app: {
    head: {
      charset: "utf-8",
      viewport: "width=device-width, initial-scale=1",
    },
    pageTransition: false,
    layoutTransition: false,
  },

  modules: ["@pinia/nuxt", "@nuxt/ui", "@nuxt/image"],

  imports: {
    dirs: ["types/**"],
  },
  plugins: ['@/plugins/youtube.client'],
  css: [
    '@/node_modules/lite-youtube-embed/src/lite-yt-embed.css'
  ],
  ui: {
    global: true,
  },
  colorMode: {
    preference: 'light'
  },
});
