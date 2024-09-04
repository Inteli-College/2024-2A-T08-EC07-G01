<script setup>
import LineChart from '@/components/Charts/LineChart.vue'
import BarChart from '@/components/Charts/BarChart.vue'
</script>

<template>
  <div class="text-center">
    <h1 class="text-center mt-10 mb-12 font-semibold text-4xl">Dashboard</h1>
    <div class="flex justify-center items-center">
      <ProgressBar class="w-80 mb-12 mt-6" />
    </div>
    <h2 class="font-semibold text-l"> Porcentagem de falhas</h2>
  </div>
  <div class="columns-2 mt-12">
    <LineChart class="w-full" />
    <BarChart/>
  </div>
</template>

  