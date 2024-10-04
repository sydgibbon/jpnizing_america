
<script setup lang="ts">
import type { classesData } from "~/types/classes/classesData";
import { useClassesStore } from "~/stores/classes"
const classesStore = useClassesStore()

const classes = [{
  name: "N5",
  classes: [{
    title: "Hiragana",
    video: "wDpsF90DoeI",
  },
  {
    title: "Katakana",
    video: "gi2AeYO-g8E",
  },
  {
    title: "Kanji",
    video: "Y13YOdclzMA",
  },]
}, {
  name: "N4",
  classes: [{
    title: "Particles",
    video: "1hTBL59rack",
  },
  {
    title: "More Particles",
    video: "Ly3Tn2MkHIQ",
  },
  {
    title: "More Kanji",
    video: "9Ux_O4xq6yk",
  },]
}, {
  name: "N3",
  classes: [{
    title: "A ton of Kanji",
    video: "7Wm8K5KrfXY",
  },
  {
    title: "A ton of grammar rules",
    video: "jd1TJALHKqg",
  },
  {
    title: "Never got this far I dunno",
    video: "qQORXsSf6SI",
  },]
}

] as classesData[];
</script>
<template>
  <div class="p-6 flex flex-wrap">
    <div class="w-full md:w-1/5 flex-col">
      <img src="~/assets/img/ura-omote-fortune-gekkan-shojo-nozaki.png" />
      <Accordion :items="classes" />
    </div>
    <div class="w-full md:w-4/5 p-6 px-auto">
      <youtube :id="classesStore.currentVideo" :key="classesStore.currentVideo"></youtube>
    </div>
  </div>
</template>
