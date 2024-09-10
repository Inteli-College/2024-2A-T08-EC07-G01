<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <h1 v-if="!knrStatus" class="text-xl font-semibold text-gray-700 mb-4">
        Digite o KNR escolhido para previsão
      </h1>
  
      <!-- Input para o KNR -->
      <div v-if="!knrStatus" class="relative w-64 mb-6">
        <input
          type="text"
          placeholder="Digite o KNR"
          v-model="knr"
          class="w-full px-4 py-2 border border-teal-500 rounded-lg focus:outline-none focus:border-teal-600"
        />
        <button class="absolute right-2 top-2 text-teal-500" @click="verificarKNR">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            class="w-6 h-6"
          >
            <path
              d="M344.5,298c15-23.6,23.8-51.6,23.8-81.7c0-84.1-68.1-152.3-152.1-152.3C132.1,64,64,132.2,64,216.3  c0,84.1,68.1,152.3,152.1,152.3c30.5,0,58.9-9,82.7-24.4l6.9-4.8L414.3,448l33.7-34.3L339.5,305.1L344.5,298z M301.4,131.2  c22.7,22.7,35.2,52.9,35.2,85c0,32.1-12.5,62.3-35.2,85c-22.7,22.7-52.9,35.2-85,35.2c-32.1,0-62.3-12.5-85-35.2  c-22.7-22.7-35.2-52.9-35.2-85c0-32.1,12.5-62.3,35.2-85c22.7-22.7,52.9-35.2,85-35.2C248.5,96,278.7,108.5,301.4,131.2z"
            />
          </svg>
        </button>
      </div>
  
      <!-- Tela de carro sem falha prevista -->
      <div v-if="knrStatus === 'sem-falha'" class="w-full max-w-lg p-8 bg-white border-2 border-green-400 rounded-lg shadow-lg">
        <div class="flex items-center mb-6">
            <svg id="Layer_1" viewBox="0 0 612 792" xmlns="http://www.w3.org/2000/svg">
                <path fill="#41AD49" d="M562,396c0-141.4-114.6-256-256-256S50,254.6,50,396s114.6,256,256,256S562,537.4,562,396L562,396z
                M501.7,296.3l-241,241l0,0l-17.2,17.2L110.3,421.3l58.8-58.8l74.5,74.5l199.4-199.4L501.7,296.3L501.7,296.3z"/>
            </svg>

          <span class="text-xl font-semibold text-green-600">Carro sem falha prevista</span>
        </div>
        <p class="text-center text-gray-700 text-xl font-medium mb-6">KNR: 7777</p>
        <p class="text-center text-gray-500 mb-4">Tipo de Falha Prevista</p>
        <div class="grid grid-cols-9 gap-4 mt-2">
          <div class="border border-gray-300 p-4 text-center">Tipo 1</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 2</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 3</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 4</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 5</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 6</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 7</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 8</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 9</div>
        </div>
      </div>
  
      <!-- Tela de carro com falha prevista -->
      <div v-if="knrStatus === 'com-falha'" class="w-full max-w-lg p-8 bg-white border-2 border-red-400 rounded-lg shadow-lg">
        <div class="flex items-center mb-6">
            <svg id="Layer_1" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
                <circle fill="#C93636" cx="64" cy="64" r="64"/>
                <path fill="#FFFFFF" d="M100.3,90.4L73.9,64l26.3-26.4c0.4-0.4,0.4-1,0-1.4l-8.5-8.5c-0.4-0.4-1-0.4-1.4,0L64,54.1L37.7,27.8
                c-0.4-0.4-1-0.4-1.4,0l-8.5,8.5c-0.4,0.4-0.4,1,0,1.4L54,64L27.7,90.3c-0.4,0.4-0.4,1,0,1.4l8.5,8.5c0.4,0.4,1.1,0.4,1.4,0L64,73.9
                l26.3,26.3c0.4,0.4,1.1,0.4,1.5,0.1l8.5-8.5C100.7,91.4,100.7,90.8,100.3,90.4z"/>
            </svg>

          <span class="text-xl font-semibold text-red-600">Carro com falha prevista</span>
        </div>
        <p class="text-center text-gray-700 text-xl font-medium mb-6">KNR: 2023-2056234</p>
        <p class="text-center text-gray-500 mb-4">Tipo de Falha Prevista</p>
        <div class="grid grid-cols-9 gap-4 mt-2">
          <div class="border border-gray-300 p-4 text-center">Tipo 1</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 2</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 3</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 4</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 5</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 6</div>
          <div class="bg-red-400 text-white border border-red-400 p-4 text-center">Tipo 7</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 8</div>
          <div class="border border-gray-300 p-4 text-center">Tipo 9</div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        knr: '',
        knrStatus: null
      };
    },
    methods: {
      verificarKNR() {
        if (this.knr === '1') {
          this.knrStatus = 'sem-falha';
        } else if (this.knr === '2') {
          this.knrStatus = 'com-falha';
        } else {
          this.knrStatus = null;
          alert('KNR inválido!');
        }
      }
    }
  };
  </script>
  