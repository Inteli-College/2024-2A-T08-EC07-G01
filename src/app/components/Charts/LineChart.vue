<script setup lang="ts">
import { ref, watch } from 'vue';
import { LineChart } from '@/components/ui/chart-line';
import { getLineChart, type DataSets } from './lineData'; // Altere para o caminho correto do arquivo LineData.ts

// Estado para o conjunto de dados
const dataSets: DataSets = getLineChart();
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
        <option value="TodasFalhas"> Todas as Falhas </option>
        <option value="Classe_1"> Falhas Classe 1</option>
        <option value="Classe_2"> Falhas Classe 2</option>
        <option value="Classe_3"> Falhas Classe 3</option>
        <option value="Classe_4"> Falhas Classe 4</option>
        <option value="Classe_5"> Falhas Classe 5</option>
        <option value="Classe_6"> Falhas Classe 6</option>
        <option value="Classe_7"> Falhas Classe 7</option>
        <option value="Classe_8"> Falhas Classe 8</option>
        <option value="Classe_9"> Falhas Classe 9</option>
      </select>
    </div>

    <!-- Gráfico de Linha -->
    <LineChart
      :data="data"
      index="year"
      :categories="['Export Growth Rate', 'Import Growth Rate']"
      :y-formatter="(tick, i) => {
        return typeof tick === 'number'
          ? `$ ${new Intl.NumberFormat('us').format(tick).toString()}`
          : ''
      }"
    />
  </div>
</template>
