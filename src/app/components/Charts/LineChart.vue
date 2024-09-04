<script setup lang="ts">
import { LineChart } from '@/components/ui/chart-line'
import { testLineChart, type TestLineChart } from './lineData';


const data = ref<TestLineChart[]>([])

data.value = testLineChart
</script>

<template>
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
</template>