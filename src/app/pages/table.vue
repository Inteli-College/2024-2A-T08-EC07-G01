<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { columns } from '../components/table/columns'
import  { fetchTestData }  from '../components/table/testData'
import type { TestData } from '../components/table/testData'
import DataTable from '../components/table/data-table.vue'

const data = ref<TestData[]>([])

onMounted(async () => {
  data.value = await fetchTestData()
})
</script>

<template>
    <div class="container py-10 mx-auto">
        <DataTable :columns="columns" :data="data" />
    </div>
</template>
