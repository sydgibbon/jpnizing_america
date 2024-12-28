<script setup>
import { ref } from 'vue'
import {
  Dialog,
} from '@headlessui/vue'
import {
  Bars3Icon,
  XMarkIcon,
} from '@heroicons/vue/24/outline'

const mobileMenuOpen = ref(false)

import { useRoute } from 'vue-router';

const route = useRoute();
const runtimeConfig = useRuntimeConfig()
</script>

<template>
  <header class="bg-white shadow-sm flex justify-between">
    <div class="px-8 py-2">
      <a href="/" class="">
        <span class="sr-only">Japonizando America</span>
        <img class="h-auto w-20" src="/img/logo.jpg" alt="" />
      </a>
    </div>
    <nav class="w-full flex items-center justify-end lg:justify-between p-6 lg:px-8" aria-label="Global">

      <div class="flex lg:hidden">
        <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          @click="mobileMenuOpen = true">
          <span class="sr-only">Open main menu</span>
          <Bars3Icon class="h-6 w-6" aria-hidden="true" />
        </button>
      </div>
      <div class="hidden lg:flex lg:gap-x-12">
        <a href="/"
          :class="['text-sm/6 font-semibold hover:text-red-500', route.path === '/' ? 'text-red-500' : 'text-gray-900']">Inicio</a>
        <a href="/programas"
          :class="['text-sm/6 font-semibold hover:text-red-500', route.path === '/programas' ? 'text-red-500' : 'text-gray-900']">Programas</a>
        <a href="/contacto"
          :class="['text-sm/6 font-semibold hover:text-red-500', route.path === '/contacto' ? 'text-red-500' : 'text-gray-900']">Contacto</a>
      </div>
      <div class="hidden lg:flex lg:flex-1 lg:justify-end">
        <a href="https://cursos.japonizandoamerica.com/login/index.php" class="text-sm/6 font-semibold text-gray-900 hover:text-red-500">Log in <span aria-hidden="true">&rarr;</span></a>
      </div>
    </nav>
    <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
      <div class="fixed inset-0 z-10" />
      <DialogPanel
        class="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between">
          <a href="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Japonizando America</span>
            <img class="h-8 w-auto" src="/img/logo.jpg" alt="" />
          </a>
          <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = false">
            <span class="sr-only">Close menu</span>
            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="mt-6 flow-root">
          <div class="-my-6 divide-y divide-gray-500/10">
            <div class="space-y-2 py-6">
              <a href="/"
                :class="['-mx-3 block rounded-lg px-3 py-2 text-base/7 font-semibold hover:bg-gray-50', route.path === '/' ? 'text-red-500' : 'text-gray-900']">
                Inicio
              </a>
              <a href="/programas"
                :class="['-mx-3 block rounded-lg px-3 py-2 text-base/7 font-semibold hover:bg-gray-50', route.path === '/programas' ? 'text-red-500' : 'text-gray-900']">
                Programas
              </a>
              <a href="/contacto"
                :class="['-mx-3 block rounded-lg px-3 py-2 text-base/7 font-semibold hover:bg-gray-50', route.path === '/contacto' ? 'text-red-500' : 'text-gray-900']">
                Contacto
              </a>
            </div>
            <div class="py-6">
              <a href="#"
                class="-mx-3 block rounded-lg px-3 py-2.5 text-base/7 font-semibold text-gray-900 hover:bg-gray-50">Log
                in</a>
            </div>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </header>
</template>
