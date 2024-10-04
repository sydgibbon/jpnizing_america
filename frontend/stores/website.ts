type websiteState = {
  name: string | null,
  description: string | null,
}
export const useWebsiteStore = defineStore('websiteStore', {
    state: () => ({
      name: '',
      description: ''
    } as websiteState),
    actions: {
      async fetch() {
        const infos = await $fetch('https://api.nuxt.com/modules/pinia') as websiteState
  
        this.name = infos.name
        this.description = infos.description
      }
    }
  })
  