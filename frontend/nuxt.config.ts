export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  $production: {
    routeRules: {
      '/**': { isr: true }
    }
  },

  $development: {
    //
  },

  runtimeConfig: {
    // The private keys which are only available server-side
    apiSecret: '123',
    // Keys within public are also exposed client-side
    public: {
      apiBase: '/api'
    }
  },

  compatibilityDate: '2024-09-29',

  webpack: {
    loaders: {
      vue: {
        hotReload: true,
      }
    }
  },

  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
    },
    pageTransition: false,
    layoutTransition: false
  },

  modules: ['@pinia/nuxt', '@nuxtjs/tailwindcss', '@nuxt/scripts'],

  imports:{
    dirs: ['types/**']
  }
})