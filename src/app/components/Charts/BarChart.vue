<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { BarChart } from '@/components/ui/chart-bar'

// Define the structure for your response data
interface ModelMetrics {
  model_name: string;
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
}

// State for your chart data and models
const data = ref<any[]>([]);
const models = ref<string[]>([]);
const selectedSet = ref<string | null>(null); // Added this to avoid v-model issues

const config = useRuntimeConfig();
const apiURL = config.public.backendUrl;

// Function to fetch data from API using fetch
const fetchData = async () => {
  try {
    const response = await fetch(`${apiURL}/api/models/current-models`); // Replace with your actual endpoint
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    const apiData: ModelMetrics[] = await response.json(); // Parse JSON from response
    console.log("apiData", apiData);

    // Transform the API data into a transposed format
    const transformedData: any[] = [
      { metric: 'accuracy', ...apiData.reduce((acc, model) => ({ ...acc, [model.model_name]: model.accuracy }), {}) },
      { metric: 'precision', ...apiData.reduce((acc, model) => ({ ...acc, [model.model_name]: model.precision }), {}) },
      { metric: 'recall', ...apiData.reduce((acc, model) => ({ ...acc, [model.model_name]: model.recall }), {}) },
      { metric: 'f1_score', ...apiData.reduce((acc, model) => ({ ...acc, [model.model_name]: model.f1_score }), {}) }
    ];

    data.value = transformedData;

    // Extract model names for the dropdown (optional)
    models.value = apiData.map((model) => model.model_name);
  } catch (error) {
    console.error("Error fetching data", error);
  }
};

// Fetch data when the component is mounted
onMounted(() => {
  fetchData();
});
</script>

<template>
  <div class="flex flex-col items-start w-full">
    <!-- Dropdown to select a specific model (optional) -->
    <div class="mb-4">
      <label for="modelSelect" class="block mb-1 font-medium text-gray-700">
        Select Model
      </label>
      <select
        id="modelSelect"
        class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
        v-model="selectedSet"
      >
        <option v-for="model in models" :key="model" :value="model">
          {{ model }}
        </option>
      </select>
    </div>

    <!-- Bar Chart -->
    <BarChart
      :data="data"
      index="metric"
      :categories="models"
      :y-formatter="(tick) => {
        return typeof tick === 'number'
          ? tick.toFixed(2)
          : ''
      }"
    />
  </div>
</template>
