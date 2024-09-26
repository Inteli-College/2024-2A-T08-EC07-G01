<script setup>
import { ref } from 'vue';  // ref para criar uma variável reativa
import LineChart from '@/components/Charts/LineChart.vue';
import BarChart from '@/components/Charts/BarChart.vue';
import PieChart from '@/components/Charts/PieChart.vue';
import Button from '~/components/ui/button/Button.vue';

// Variável reativa para controlar a visualização (falhas ou modelos)
const currentView = ref('falhas');  // 'falhas' será o valor inicial

// Função para alterar a visualização
const handleViewChange = (view) => {
  currentView.value = view;  // Atualiza a visualização com o novo valor
};
</script>

<template>
  <div class="text-center">
    <h1 class="text-center mt-10 mb-12 font-semibold text-4xl">Dashboard</h1>

    <!-- Botões para alternar entre Falhas e Modelos -->
      <div class="flex justify-center gap-3">
        <Button
          class="bg-customGreen text-white transition-all duration-300" 
          :class="{
            'bg-transparent border-2 border-customGreen text-customGreen': currentView === 'falhas',
            'hover:bg-transparent hover:border-2 hover:border-customGreen hover:text-customGreen': currentView !== 'falhas'
          }" 
          @click="handleViewChange('falhas')"
        >
          Falhas
        </Button>

        <Button
          class="bg-customGreen text-white transition-all duration-300"
          :class="{
            'bg-transparent border-2 border-customGreen text-customGreen': currentView === 'modelos',
            'hover:bg-transparent hover:border-2 hover:border-customGreen hover:text-customGreen': currentView !== 'modelos'
          }" 
          @click="handleViewChange('modelos')"
        >
          Modelos
        </Button>
      </div>



    <!-- Barra de progresso e título -->
    <h2 class="font-semibold text-l">Porcentagem de falhas</h2>

    <!-- Gráficos -->
    <div class="flex mt-12 px-8">
      <!-- Exibe os gráficos com base no valor de currentView -->
      <template v-if="currentView === 'falhas'">
        <div class="flex items-center">
          <div class="flex gap-6 w-full">

            <div class="flex flex-col gap-3">
              <h2>Quantidade de Falhas por Carros analisados</h2>
              <PieChart />
            </div>

            <div class="flex flex-col gap-3">
              <h2>Classes de Falhas por Total de falhas</h2>
              <PieChart />
            </div>
            
            <div class="flex flex-col gap-3 w-full">
              <h2>Quantidade de Falhas por tempo</h2>
              <LineChart class=" w-full"/>
            </div>

          </div>
        </div>
      </template>

      
      <template v-if="currentView === 'modelos'">
        <div class="flex items-center">
          <div class="flex gap-6 w-full">

            <div class="flex flex-col gap-3">
              <h2>Quantidade de Falhas por Carros analisados</h2>
              <BarChart/>
            </div>

            <div class="flex flex-col gap-3">
              <h2>Classes de Falhas por Total de falhas</h2>
              <PieChart />
            </div>
            
            <div class="flex flex-col gap-3 w-full">
              <h2>Quantidade de Falhas por tempo</h2>
              <LineChart class=" w-full"/>
            </div>

          </div>
        </div>
      </template>
    </div>
  </div>
</template>
