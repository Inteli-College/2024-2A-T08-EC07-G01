<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-4xl w-full">
        <h3 class="text-customBlue text-2xl font-bold mb-4">Escolha do Modelo {{ selectedModel.name }}</h3>
        <h4 class="text-customBlue text-xl font-semibold mb-4">Escolhas recomendadas</h4>
        
        <table class="border-collapse border border-gray-300 w-full">
          <thead class="bg-gray-100">
            <tr>
              <th class="border border-gray-300 px-4 py-2">Modelos</th>
              <th class="border border-gray-300 px-4 py-2">Acurácia</th>
              <th class="border border-gray-300 px-4 py-2">Recall</th>
              <th class="border border-gray-300 px-4 py-2">F1</th>
              <th class="border border-gray-300 px-4 py-2">Precisão</th>
              <th class="border border-gray-300 px-4 py-2">Escolha</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(model, index) in models" :key="index">
              <td class="border border-gray-300 px-4 py-2">{{ model.name }}</td>
              <td class="border border-gray-300 px-4 py-2">{{ model.accuracy }}</td>
              <td class="border border-gray-300 px-4 py-2">{{ model.recall }}</td>
              <td class="border border-gray-300 px-4 py-2">{{ model.f1 }}</td>
              <td class="border border-gray-300 px-4 py-2">{{ model.precision }}</td>
              <td class="border border-gray-300 px-4 py-2 text-center">
                <input type="radio" name="modelSelect" />
              </td>
            </tr>
          </tbody>
        </table>
        
        <button class="mt-4 bg-customBlue text-white px-4 py-2 rounded-lg
        flex items-center space-x-2 rounded-lg px-4 py-3 cursor-pointer transition-all duration-300 hover:bg-customGreen hover:border-2 hover:border-customGreen" @click="$emit('close')">Fechar</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      selectedModel: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        models: [
          { name: "Anamodel2024332424", accuracy: "94%", recall: "94%", f1: "94%", precision: "94%" },
          { name: "Ivanmodel32142132321", accuracy: "93%", recall: "93%", f1: "93%", precision: "93%" },
          { name: "Brenomodel321312312", accuracy: "92%", recall: "92%", f1: "92%", precision: "92%" },
          { name: "Brenomodel321312312", accuracy: "91%", recall: "91%", f1: "91%", precision: "91%" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .fixed {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }
  </style>

