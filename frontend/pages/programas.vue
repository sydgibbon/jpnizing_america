<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold text-red-500 text-center mb-12">Nuestros Programas</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Taller de Conversación -->
      <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
        <div class="flex items-start gap-4">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center">
            <span class="text-2xl">🗣️</span>
          </div>
          <div>
            <h3 class="font-bold text-xl text-red-500 mb-2">TALLER DE CONVERSACIÓN</h3>
            <p class="text-gray-600">¡Vive la experiencia de hablar en japonés con tus compañeros y habla de lo que te gusta!</p>
          </div>
        </div>
      </div>

      <!-- Taller de Ver Anime -->
      <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
        <div class="flex items-start gap-4">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center">
            <span class="text-2xl">😎</span>
          </div>
          <div>
            <h3 class="font-bold text-xl text-red-500 mb-2">TALLER DE VER ANIME SIN SUB</h3>
            <p class="text-gray-600">Pon a prueba tu conocimiento con capítulos y series increíbles</p>
          </div>
        </div>
      </div>

      <!-- Curso de Kanji -->
      <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
        <div class="flex items-start gap-4">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center">
            <span class="text-2xl">🈸</span>
          </div>
          <div>
            <h3 class="font-bold text-xl text-red-500 mb-2">CURSO DE KANJI</h3>
            <p class="text-gray-600">Aprende el arte del kanji, y domínalos como un japo nativo.</p>
          </div>
        </div>
      </div>

      <!-- Cursos JLPT -->
      <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
        <div class="flex items-start gap-4">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center">
            <span class="text-2xl">📚</span>
          </div>
          <div>
            <h3 class="font-bold text-xl text-red-500 mb-2">CURSOS JLPT</h3>
            <ul class="space-y-2 text-gray-600">
              <li>• CURSO N5: Desarrolla las habilidades de comunicación básica</li>
              <li>• CURSO N4: Eleva tu nivel de comunicación semi-intermedia</li>
              <li>• CURSO N3: ¡Cada vez más cerca del nativo! Comunicación intermedia</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Cursos Preparatorios -->
      <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
        <div class="flex items-start gap-4">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center">
            <span class="text-2xl">👨🏻‍🎓</span>
          </div>
          <div>
            <h3 class="font-bold text-xl text-red-500 mb-2">CURSOS PREPARATORIOS JLPT</h3>
            <ul class="space-y-2 text-gray-600">
              <li>• CURSO PREPARATORIO N5: Prepárate para rendir el JLPT N5</li>
              <li>• CURSO PREPARATORIO N4: Prepárate para rendir el JLPT N4</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>