<template>
  <iframe
    id="ytplayer"
    type="text/html"
    width="100%"
    height="400px"
    :src="`https://www.youtube.com/embed/${videoLink}?autoplay=${autoplay}&origin=https://japonizandoamerica.com`"
    frameborder="0"
  />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    id: String,
    label: String,
    autoplay: {
      type: String,
      default: "0",
    },
    videoLink: {
      type: String,
      required: true,
    },
  },
  fetchOnServer: false,
});
</script>