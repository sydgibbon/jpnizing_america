import { defineStore } from 'pinia';
type authState = {
  token: string | null,
  user: string | null,
}
export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
    user: null,
  } as authState),
  actions: {
    login(token: string | null ) {
      this.token = token;
    },
    logout() {
      this.token = null;
      this.user = null;
    },
  },
});
