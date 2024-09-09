<template>
    <transition name="modal">
      <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50">
        <div class="bg-white rounded-lg p-6 w-full max-w-4xl shadow-lg">

          <button class="top-4 right-4 hover:scale-[110%]" @click="close">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
  

          <h2 class="text-center text-2xl font-semibold mb-6">Arquivo adicionado com sucesso</h2>
  

          <div class="grid grid-cols-2 gap-6">

            <div>
              <h3 class="text-center font-medium mb-4">Métricas do Modelo Anterior</h3>
              <div class="space-y-2">
                <div class="bg-gray-200 p-4 rounded-md text-center">Acurácia: 0.8752</div>
                <div class="bg-gray-200 p-4 rounded-md text-center">Precisão: 0.9212</div>
                <div class="bg-gray-300 p-4 rounded-md text-center">Recall: 0.9056</div>
                <div class="bg-gray-200 p-4 rounded-md text-center">F1-score: 0.9056</div>
              </div>
            </div>
  

            <div>
              <h3 class="text-center font-medium mb-4">Métricas do Modelo Atualmente</h3>
              <div class="space-y-2">
                <div class="bg-green-200 p-4 rounded-md text-center flex items-center justify-center">Acurácia: 0.8921 <span class="ml-2 text-green-500">⬆</span></div>
                <div class="bg-red-200 p-4 rounded-md text-center flex items-center justify-center">Precisão: 0.9017 <span class="ml-2 text-red-500">⬇</span></div>
                <div class="bg-red-200 p-4 rounded-md text-center flex items-center justify-center">Recall: 0.8811 <span class="ml-2 text-red-500">⬇</span></div>
                <div class="bg-green-200 p-4 rounded-md text-center flex items-center justify-center">F1-score: 0.9256 <span class="ml-2 text-green-500">⬆</span></div>
              </div>
            </div>
          </div>
  
          <div class="flex justify-center mt-6">
            <button class="bg-teal-600 hover:bg-teal-700 text-white font-semibold py-2 px-6 rounded-md flex items-center" @click="revert">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v6h6M20 20v-6h-6M16 8h2a2 2 0 012 2v10a2 2 0 01-2 2H8a2 2 0 01-2-2v-2M8 4h2M5 9l-5-5m0 0L5 9M15 15l5 5m0 0-5-5" />
              </svg>
              Reverter
            </button>
          </div>
        </div>
      </div>
    </transition>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue'
  

  const props = defineProps({
    show: {
      type: Boolean,
      required: true
    }
  })
  
  const emit = defineEmits(['close', 'revert'])
  
  const close = () => {
    emit('close')
  }
  
  const revert = () => {
    emit('revert')
  }
  </script>
  
  <style scoped>
  .modal-enter-active, .modal-leave-active {
    transition: opacity 0.3s ease;
  }
  .modal-enter, .modal-leave-to {
    opacity: 0;
  }
  </style>
  