export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
    'shadcn-nuxt',
    '@nuxt/icon',
    '@vueuse/motion/nuxt',
    'nuxt-security'
  ],

  shadcn: {
    prefix: '',
    componentDir: './components/ui'
  },

  security: {
    corsHandler: {
      origin: '*',
      methods: '*',
      credentials: true
    }
  },

  compatibilityDate: '2024-08-20',

  // Add this for environment variables
  runtimeConfig: {
    public: {
      backendUrl: process.env.BACKEND_URL
    }
  }
});
