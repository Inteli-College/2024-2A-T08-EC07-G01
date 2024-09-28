<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { BarChart } from '@/components/ui/chart-bar'
import { getBarChart, type DataSets } from './BarData' // Certifique-se de que o caminho do arquivo está correto

// Estado para o conjunto de dados
const dataSets: DataSets = getBarChart();
const selectedSet = ref<keyof DataSets>('YN'); // Valor inicial definido
const data = ref(dataSets[selectedSet.value]);

// Função para atualizar os dados com base na seleção
const updateData = (event: Event) => {
  const target = event.target as HTMLSelectElement;
  selectedSet.value = target.value as keyof DataSets;
  data.value = dataSets[selectedSet.value];
}

// Ao montar o componente, garanta que o gráfico inicial seja exibido
onMounted(() => {
  data.value = dataSets[selectedSet.value];
});
</script>

<template>
  <div class="flex flex-col items-start w-full">
    <!-- Dropdown para selecionar o conjunto de dados -->
    <div class="mb-4">
      <label for="dataSelect" class="block mb-1 font-medium text-gray-700">Selecione o Conjunto de Dados</label>
      <select
        id="dataSelect"
        @change="updateData"
        class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        v-model="selectedSet"
      >
        <option value="YN">Modelo Yes or No</option>
        <option value="Classe_1">Modelo Classe 1</option>
        <option value="Classe_2">Modelo Classe 2</option>
        <option value="Classe_3">Modelo Classe 3</option>
        <option value="Classe_4">Modelo Classe 4</option>
        <option value="Classe_5">Modelo Classe 5</option>
        <option value="Classe_6">Modelo Classe 6</option>
        <option value="Classe_7">Modelo Classe 7</option>
        <option value="Classe_8">Modelo Classe 8</option>
        <option value="Classe_9">Modelo Classe 9</option>
      </select>
    </div>

    <!-- Gráfico de Barras -->
    <BarChart
      :data="data"
      index="name"
      :categories="['total', 'predicted']"
      :y-formatter="(tick, i) => {
        return typeof tick === 'number'
          ? `$ ${new Intl.NumberFormat('us').format(tick).toString()}` 
          : ''
      }"
    />
  </div>
</template>
