export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
    'shadcn-nuxt',
    "@nuxt/icon",
    "@vueuse/motion/nuxt",
    'nuxt-security'
  ],

  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  },

  security: {
    corsHandler: {
      origin: 'http://localhost:3001',
      methods: '*',
      credentials: true

    }
  },

  compatibilityDate: '2024-08-20'
})
