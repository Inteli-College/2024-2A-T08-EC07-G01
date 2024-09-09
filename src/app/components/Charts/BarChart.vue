<script setup lang="ts">
import { AreaChart } from '@/components/ui/chart-area'
import ChartTooltip from '../ChartTooltip.vue';
import { getTestBarChart, type TestBarChart } from './barData';

const data = ref<TestBarChart[]>([])

data.value = getTestBarChart()
</script>

<template>
  <AreaChart :data="data" index="name" :categories="['total', 'predicted']" :custom-tooltip="ChartTooltip"/>
</template>