<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { columns } from '../components/table/columns'
import { TestData } from '../components/table/testData'
import DataTable from '../components/table/data-table.vue'

const data = ref<TestData[]>([])

onMounted(() => {
    data.value = TestData // Use the sample data provided
})
</script>

<template>
    <div class="container py-10 mx-auto">
        <DataTable :columns="columns" :data="data" />
    </div>
</template>
