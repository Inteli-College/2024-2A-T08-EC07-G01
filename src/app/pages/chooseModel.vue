<template>
    <div class="flex flex-col justify-center items-center mt-10">
      <h1 class="text-center mt-10 mb-12 font-semibold text-4xl">Escolha dos Modelos</h1>
  
      <div class="space-y-4 w-full max-w-xl">
        <div
          v-for="(modelClass, index) in modelClasses"
          :key="index"
          class="flex items-center space-x-2 bg-customBlue rounded-lg px-4 py-3 cursor-pointer transition-all duration-300 hover:bg-customGreen hover:border-2 hover:border-customGreen hover:text-customGreen"
          @click="openModal(modelClass)"
        >
          <p class="text-white flex-grow">{{ modelClass.name }}</p>
          <p class="bg-white text-customBlue rounded-lg p-2">
            {{ selectedModels[index] || 'Selecione um modelo' }}
          </p>
        </div>
      </div>
  
      <choose-model-modal
        v-if="isModalOpen"
        :selectedModel="selectedModel"
        @model-selected="updateSelectedModel"
        @close="closeModal"
      />
    </div>
  </template>
  
  <script>
  import ChooseModelModal from '@/components/Modal/chooseModelModal.vue';
  
  export default {
    components: {
      ChooseModelModal,
    },
    data() {
      return {
        isModalOpen: false,
        selectedModel: null,
        selectedModels: [],
        modelClasses: [
          { name: "Modelo Y/N" },
          { name: "Classe 1" },
          { name: "Classe 2" },
          { name: "Classe 3" },
          { name: "Classe 4" },
          { name: "Classe 5" },
          { name: "Classe 6" },
          { name: "Classe 7" },
          { name: "Classe 8" },
          { name: "Classe 9" },
        ],
      };
    },
    methods: {
      openModal(index) {
        this.selectedModel = { ...this.modelClasses[index], index };
        this.isModalOpen = true;
      },
      updateSelectedModel(model) {
        this.$set(this.selectedModels, model.index, model.name);
      },
      closeModal() {
        this.isModalOpen = false;
      },
    },
  };
  </script>
  
  <style scoped>

  </style>

