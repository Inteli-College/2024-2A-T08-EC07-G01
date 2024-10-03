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
          { name: "Modelo Y/N", apiEndpoint: "/api/models/best-metrics/type0" },
          { name: "Classe 1", apiEndpoint: "/api/models/best-metrics/type1" },
          { name: "Classe 2", apiEndpoint: "/api/models/best-metrics/type2" },
          { name: "Classe 3", apiEndpoint: "/api/models/best-metrics/type3" },
          { name: "Classe 4", apiEndpoint: "/api/models/best-metrics/type4" },
          { name: "Classe 5", apiEndpoint: "/api/models/best-metrics/type5" },
          { name: "Classe 6", apiEndpoint: "/api/models/best-metrics/type6" },
          { name: "Classe 7", apiEndpoint: "/api/models/best-metrics/type7" },
          { name: "Classe 8", apiEndpoint: "/api/models/best-metrics/type8" },
          { name: "Classe 9", apiEndpoint: "/api/models/best-metrics/type9" },
        ],
      };
    },
    methods: {
      openModal(modelClass) {
        this.selectedModel = { ...modelClass };
        this.isModalOpen = true;
      },
      updateSelectedModel(model) {
        const index = this.modelClasses.findIndex((m) => m.name === this.selectedModel.name);
        this.$set(this.selectedModels, index, model.model_name);
      },
      closeModal() {
        this.isModalOpen = false;
      },
    },
  };
  </script>
  
  <style scoped>

  </style>

