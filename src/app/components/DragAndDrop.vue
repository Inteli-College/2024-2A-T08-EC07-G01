<template>
    <div 
      class="relative flex flex-col items-center justify-center border-4 border-dashed border-gray-300 rounded-xl p-8 w-full max-w-lg mx-auto cursor-pointer hover:border-green-500 transition duration-300 ease-in-out bg-white shadow-lg"
      @dragover.prevent="handleDragOver"
      @dragleave.prevent="handleDragLeave"
      @drop.prevent="handleDrop"
      @click="triggerFileInput"
    >
      <div v-if="isDragging" class="absolute inset-0 bg-green-100 opacity-50 rounded-xl pointer-events-none"></div>
  
      <div class="text-center z-10" :class="{'text-green-500': isDragging}" v-if="!file">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto mb-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v4a1 1 0 001 1h3m10 0h3a1 1 0 001-1V7m-4 10l-4 4m0 0l-4-4m4 4V4" />
        </svg>
        <h2 class="text-2xl font-semibold text-gray-700">Drag & Drop Files Here</h2>
        <p class="mt-1 text-gray-500">or click to upload</p>
      </div>
  
      <input ref="fileInput" type="file" class="file-input" @change="handleFileUpload" />
  
      <div v-if="file" class="w-full mt-4">
        <p class="text-gray-600 font-semibold">{{ file.name }} ({{ formatFileSize(file.size) }})</p>
  
        <Progress
          class="mt-2"
          :modelValue="uploadProgress"
          aria-label="File Upload Progress"
        />
  
        <Button class="mt-4 w-full" @click="handleContinue" :disabled="uploadProgress < 100">Continue</Button>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  
  const file = ref<File | null>(null)
  const uploadProgress = ref<number>(0)
  
  const isDragging = ref(false)
  const handleDragOver = () => (isDragging.value = true)
  const handleDragLeave = () => (isDragging.value = false)
  const handleDrop = (event: DragEvent) => {
    event.preventDefault()
    isDragging.value = false
    const droppedFiles = Array.from(event.dataTransfer?.files || [])
    file.value = droppedFiles[0]
    simulateUpload()
  }
  
  const triggerFileInput = () => {
    const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement
    if (fileInput) {
      fileInput.click()
    }
  }
  
  const handleFileUpload = (event: Event) => {
    const input = event.target as HTMLInputElement
    const uploadedFiles = Array.from(input.files || [])
    file.value = uploadedFiles[0]
    simulateUpload()
  }
  
  const simulateUpload = () => {
    uploadProgress.value = 0
    const intervalId = setInterval(() => {
      if (uploadProgress.value < 100) {
        uploadProgress.value += 20 // Aumenta progresso da barra em 20% a cada 100ms (é fazivel pra integrar)
      } else {
        clearInterval(intervalId)
      }
    }, 100)
  }
  
  const formatFileSize = (size: number) => {
    const kb = size / 1024
    return kb > 1024 ? `${(kb / 1024).toFixed(2)} MB` : `${kb.toFixed(2)} KB`
  }
  
  const handleContinue = () => {
    if (uploadProgress.value === 100) {
      alert('Upload complete! Continue clicked.')
    }
  }
  </script>
  
  <style scoped>
  /* Inferno pra esconder os bgl do input de file */
  input[type="file"]::file-selector-button {
    display: none;
  }
  
  input[type="file"] {
    display: none;
  }
  </style>
  