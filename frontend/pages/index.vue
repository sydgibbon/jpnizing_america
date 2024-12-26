<script setup lang="ts">
</script>

<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Hero Section -->
    <section class="text-center mb-16">
      <h1 class="text-4xl font-bold text-red-500 mb-4">
        ¡Aprender japonés con anime, sí se puede!
      </h1>
      <p class="text-xl text-gray-700 mb-8">
        Japonizando América es el único instituto donde podrás aprender japonés, fácil, rápido, ¡con manga y anime!
      </p>
      <div class="aspect-video bg-gray-200 max-w-3xl mx-auto">
        <Youtube video-link="d-7dBycGdjg" autoplay="1"/>
      </div>
    </section>

    <!-- Alumnos en Acción Section -->
    <section class="mb-16">
      <h2 class="text-3xl font-bold text-red-500 mb-8 text-center">
        ¡MIRA NUESTROS ALUMNOS EN ACCIÓN!
      </h2>
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-white rounded-lg shadow-md pb-4">
          <div class="aspect-square overflow-hidden rounded-full mx-4 mt-4 bg-gray-200 mb-4">
            <img src="~/assets/img/conversation-crop.png"/>
          </div>
          <h3 class="font-semibold px-4">Taller de Conversación</h3>
        </div>
        <div class="bg-white rounded-lg shadow-md pb-4">
          <div class="aspect-square overflow-hidden rounded-full mx-4 mt-4 bg-gray-200 mb-4">
            <img src="~/assets/img/kanji-crop.jpeg"/>
          </div>
          <h3 class="font-semibold px-4">Taller de Kanji</h3>
        </div>
        <div class="bg-white rounded-lg shadow-md pb-4">
          <div class="aspect-square overflow-hidden rounded-full mx-4 mt-4 bg-gray-200 mb-4">
            <img src="~/assets/img/podcast-crop.jpeg"/>
          </div>
          <h3 class="font-semibold px-4">Podcast en Japonés</h3>
        </div>
        <div class="bg-white rounded-lg shadow-md pb-4">
          <div class="aspect-square overflow-hidden rounded-full mx-4 mt-4 bg-gray-200 mb-4">
            <img src="~/assets/img/student_group-crop.png"/>
          </div>
          <h3 class="font-semibold px-4">¡Ellos nos recomiendan!</h3>
        </div>
      </div>
    </section>

    <!-- Demo Class Section -->
    <section class="mb-16 text-center">
      <h2 class="text-2xl font-bold text-red-500 mb-4">¿Aún no te convencemos?</h2>
      <p class="mb-4">¡Te dejamos una clase completa aquí abajo!</p>
      <div class="aspect-video bg-gray-200 max-w-3xl mx-auto">
        <Youtube video-link="WAqsJpqRGkY" autoplay="0"/>
      </div>
    </section>

    <!-- Senseis Section -->
    <section class="mb-16">
      <h2 class="text-3xl font-bold text-red-500 mb-8 text-center">NUESTROS SENSEI</h2>
      <div class="grid md:grid-cols-3 gap-8">
        <div class="text-center">
          <div class="w-48 h-48 bg-gray-200 rounded-full mx-auto mb-4">
            <img class="object-fill rounded-full" src="~/assets/img/FRAN.jpg"/>
          </div>
          <h3 class="font-bold">FRAN</h3>
          <p class="text-gray-600">JLPT N3</p>
        </div>
        <div class="text-center">
          <div class="w-48 h-48 bg-gray-200 rounded-full mx-auto mb-4">
            <img class="object-fill rounded-full" src="~/assets/img/ANTO.jpg"/>
          </div>
          <h3 class="font-bold">ANTO</h3>
          <p class="text-gray-600">JLPT N2</p>
        </div>
        <div class="text-center">
          <div class="w-48 h-48 bg-gray-200 rounded-full mx-auto mb-4">
            <img class="object-fill rounded-full" src="~/assets/img/DANI.jpg"/>
          </div>
          <h3 class="font-bold">DANI</h3>
          <p class="text-gray-600">JLPT N3</p>
        </div>
      </div>
    </section>

    <!-- Instagram Section -->
    <section class="mb-8">
      <h2 class="text-3xl font-bold text-red-500 mb-8 text-center">
        ¿QUERÉS APRENDER UN POCO MÁS?
      </h2>
      <p class="text-center text-gray-600 mb-8">
        <a href="https://www.instagram.com/japonizandoamerica/" target="_blank" class="hover:text-red-500 transition">
          ¡MIRÁ NUESTROS VIDEOS EN INSTAGRAM!
        </a>
      </p>
      <Instagram />
    </section>

    <!-- CTA Section -->
    <section class="text-center mb-16">
      <h2 class="text-2xl font-bold text-red-500 mb-4">
        ¿Qué esperas para comenzar tu viaje con nosotros?
      </h2>
      <a href="https://wa.me/+5493513401855" target="_blank" class="inline-block bg-red-500 text-white px-8 py-3 rounded-lg hover:bg-red-600 transition">
        ¡Mandanos MD!
      </a>
    </section>
  </div>
</template>