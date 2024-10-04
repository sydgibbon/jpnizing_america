<template>
    <div>
      <div v-for="(item, sectionIdx) in list" :key="sectionIdx">
        <h2>
          <button
            @click="openOrClose(item)"
            type="button"
            class="flex w-full items-center justify-between border border-gray-200 p-5 text-left font-medium text-gray-500 hover:bg-gray-100"
            :class="{
              'rounded-t-xl': sectionIdx === 0,
              'border-b-0': questionBorder(sectionIdx, item, items),
              'bg-gray-100': item.open,
              'bg-white': !item.open
            }"
          >
            <span>{{ item.name }}</span>
            <Icon name="mdi:chevron-down" />
          </button>
        </h2>
  
        <div class="bg-white" :class="{ hidden: !item.open }">
          <button v-for="courseClass, classIdx in item.classes"
            @click="selectClass(sectionIdx, classIdx, list)"
            class="flex w-full items-center justify-between border border-gray-200 p-5 text-left font-medium text-gray-500 hover:bg-gray-100"
            :class="{
              'bg-gray-100': courseClass.selected,
              'bg-white': (!courseClass.selected)
            }"
          >
            <p class="text-gray-500">{{ courseClass.title }}</p>
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import type { classesData, classData } from "~/types/classes/classesData";
  const props = defineProps<{
    items: classesData[]
  }>();
  

  let selectedSection: number | null = null
  let selectedClass: number | null = null

  const list = ref(
    props.items.map((item) => {
      return { ...item, open: false };
    })
  );


  function openOrClose(item: classesData) {
    item.open = !item.open;
  }

  function selectClass(sectionIdx:number, classIdx: number, sections:classesData[]) {
    if (selectedClass !== null && selectedSection !== null){
      sections[selectedSection].classes[selectedClass].selected = false;
    }
    selectedClass= classIdx;
    selectedSection= sectionIdx;
    sections[sectionIdx].classes[classIdx].selected = true;
  }
  
  function questionBorder(idx:number, item: classesData, items:classesData[]) {
    if (idx < items.length - 1 && !item.open) return true;
  }
  </script>