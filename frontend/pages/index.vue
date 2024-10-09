<script setup lang="ts">
import type { classesData } from "~/types/classes/classesData";
import { useClassesStore } from "~/stores/classes"
const classesStore = useClassesStore()

const levels = [
  {
    label: "N5",
    slot: "n5",
  },
  {
    label: "N4",
    slot: "n4",
  },
  {
    label: "N3",
    slot: "n3",
  }
] as any;

const videos = [{
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

const setVideo = (videoId: string) => {
  classesStore.setVideo(videoId); // Método que actualiza el video en el store
}
</script>
<template>
  <div class="p-6 flex flex-wrap">
    <div class="w-full md:w-1/5 flex-col">
      <img src="~/assets/img/ura-omote-fortune-gekkan-shojo-nozaki.png" />
      <UAccordion :items="levels" variant="solid">
        <template #n5>
          <UContainer>
            <ul>
              <li v-for="(video, index) in videos[0].classes" :key="video.video">
                <button @click="setVideo(video.video)">
                  {{ video.title }}
                </button>
                <UDivider v-if="index < videos[2].classes.length - 1" />
              </li>
            </ul>
          </UContainer>
        </template>
        <template #n4>
          <UContainer>
            <ul>
              <li v-for="(video, index) in videos[1].classes" :key="video.video">
                <button @click="setVideo(video.video)">
                  {{ video.title }}
                </button>
                <UDivider v-if="index < videos[2].classes.length - 1" />
              </li>
            </ul>
          </UContainer>
        </template>
        <template #n3>
          <UContainer>
            <ul>
              <li v-for="(video, index) in videos[2].classes" :key="video.video">
                <button @click="setVideo(video.video)">
                  {{ video.title }}
                </button>
                <UDivider v-if="index < videos[2].classes.length - 1" />
              </li>
            </ul>
          </UContainer>
        </template>
      </UAccordion>
    </div>
    <div class="w-full md:w-4/5 p-6 px-auto">
      <youtube :id="classesStore.currentVideo" :key="classesStore.currentVideo"></youtube>
    </div>
  </div>
</template>
