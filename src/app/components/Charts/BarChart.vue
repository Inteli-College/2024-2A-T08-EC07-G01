<script setup lang="ts">
import { ref, watch } from 'vue'
import { BarChart } from '@/components/ui/chart-bar'
import { getBarChart, type DataSets } from './BarData' // Altere para o caminho correto do arquivo barData.ts

// Estado para o conjunto de dados
const dataSets: DataSets = getBarChart();
const selectedSet = ref<keyof DataSets>('set1');
const data = ref(dataSets[selectedSet.value]);

// Função para atualizar os dados com base na seleção
const updateData = (event: Event) => {
  const target = event.target as HTMLSelectElement;
  selectedSet.value = target.value as keyof DataSets;
  data.value = dataSets[selectedSet.value];
}

// Watcher para atualizar os dados sempre que selectedSet mudar
watch(selectedSet, (newSet) => {
  data.value = dataSets[newSet];
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
      >
        <option value="set1">Conjunto de Dados 1</option>
        <option value="set2">Conjunto de Dados 2</option>
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
