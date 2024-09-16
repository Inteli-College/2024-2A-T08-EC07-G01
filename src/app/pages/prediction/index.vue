<script setup lang="ts">
import { ref } from 'vue';

const knr = ref('');
const knrStatus = ref('');
const failureType = ref('');

function verificarKNR() {
  // Simular a verificação do KNR e definir o status com base nos dados mockados
  const falhaSimulada = ['12345', '67890']; // KNRs simulados com falha
  if (falhaSimulada.includes(knr.value)) {
    knrStatus.value = 'com-falha';
    failureType.value = 'Tipo 1'; // Simulação do tipo de falha
  } else {
    knrStatus.value = 'sem-falha';
  }
}

function voltar() {
  // Resetar os dados e voltar para a tela de pesquisa
  knr.value = '';
  knrStatus.value = '';
  failureType.value = '';
}
</script>


<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50">
    <h1 v-if="!knrStatus" class="text-xl font-semibold text-gray-700 mb-4">
      Digite o KNR escolhido para previsão
    </h1>

    <!-- Tela de pesquisa -->
    <div v-if="!knrStatus" class="relative w-64 mb-6">
      <input
        type="text"
        placeholder="Digite o KNR"
        v-model="knr"
        @keyup.enter="verificarKNR"
        class="w-full px-4 py-2 border border-teal-500 rounded-lg focus:outline-none focus:border-teal-600"
      />
      <button class="absolute right-2 top-2 text-teal-500" @click="verificarKNR">
        🔍
      </button>
    </div>

    <!-- Tela de resultado sem falha -->
    <div v-if="knrStatus === 'sem-falha'" class="w-full max-w-4xl p-8 bg-white border-2 border-green-400 rounded-lg shadow-lg">
      <div class="flex items-center gap-4 mb-6">
        <span class="text-xl font-semibold text-green-600">Carro sem falha prevista</span>
      </div>
      <p class="text-center text-gray-700 text-xl font-medium mb-6">KNR: {{ knr }}</p>
      <p class="text-center text-gray-500 mb-4">Tipo de Falha Prevista</p>
      <div class="grid grid-cols-9 gap-4 mt-2">
        <!-- Suas falhas aqui -->
      </div>
      <!-- Botão de Voltar -->
      <button @click="voltar" class="mt-4 px-4 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600">
        Voltar
      </button>
    </div>

    <!-- Tela de resultado com falha -->
    <div v-if="knrStatus === 'com-falha'" class="w-full max-w-4xl p-8 bg-white border-2 border-red-400 rounded-lg shadow-lg">
      <div class="flex items-center gap-4 mb-6">
        <span class="text-xl font-semibold text-red-600">Carro com falha prevista</span>
      </div>
      <p class="text-center text-gray-700 text-xl font-medium mb-6">KNR: {{ knr }}</p>
      <p class="text-center text-gray-500 mb-4">Tipo de Falha: {{ failureType }}</p>
      <div class="grid grid-cols-9 gap-4 mt-2">
        <div v-for="i in 9" :key="i" :class="['border', 'px-6', 'text-center', failureType === 'Tipo ' + i ? 'bg-red-400 text-white border-red-400' : 'border-gray-300']">
          Tipo {{ i }}
        </div>
      </div>
      <!-- Botão de Voltar -->
      <button @click="voltar" class="mt-4 px-4 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600">
        Voltar
      </button>
    </div>
  </div>
</template>



  

  <!-- ---------------------------- -->
<!--    
Código do Barreto:

   <script setup lang="ts">
import { ref } from 'vue';

const knr = ref('');

const goToPrediction = () => {
    if (knr.value.trim()) {
        navigateTo(`/prediction/${knr.value}`);
    }
};
</script> -->


<!-- Código do Barreto2:

<script setup>
import Axios from 'axios';

const knr = useRoute().params.knr;

const styles = {
    default: {
        border: 'border-gray-300',
        bg: '',
        text: 'text-gray-800'
    },
    success: {
        border: 'border-green-500',
        bg: 'bg-green-500',
        text: 'text-white'
    },
    fail: {
        border: 'border-rose-500',
        bg: 'bg-rose-500',
        text: 'text-white'
    }
};


const res = await Axios.get(`http://localhost:8000/api/knr/${knr}`);

const failType = res.data.predicted_fail_code;

onMounted(() => {
    failTypes.value.forEach((fail) => {
        if (fail.failType === failType) {
            fail.status = 'fail';
        }
    });
});

const result = computed(() => (failType !== 0 ? 'fail' : 'success'));
const resultStyle = computed(() => styles[result.value]);
const resultText = computed(() => (result.value === 'fail' ? 'Falha prevista' : 'Sem falha prevista'));

const failTypes = ref([
    {
        failType: 1,
        title: 'Tipo 1',
        description: 'tempo na tela',
        status: 'default'
    },
    {
        failType: 2,
        title: 'Tipo 2',
        description: 'tempo na tela',
        status: 'default'
    },
    {
        failType: 3,
        title: 'Tipo 3',
        description: 'tempo na tela',
        status: 'default'
    },
    {
        failType: 4,
        title: 'Tipo 4',
        description: 'tempo na tela',
        status: 'default'
    },
    {
        failType: 5,
        title: 'Tipo 5',
        description: 'tempo na tela',
        status: 'default'
    },
    {
        failType: 6,
        title: 'Tipo 6',
        description: 'tempo na tela',
        status: 'default'
    },
    {
        failType: 7,
        title: 'Tipo 7',
        description: 'tempo na tela',
        status: 'default'
    }
]);

</script> -->