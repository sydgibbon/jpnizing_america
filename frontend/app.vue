<script setup lang="ts">
// ---cut-start---
const useColor = () => useState<string>('color', () => 'pink')
// ---cut-end---
const color = useColor() // Same as useState('color')
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>