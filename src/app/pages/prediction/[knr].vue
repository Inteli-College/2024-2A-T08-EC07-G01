<!--TODO: Type component-->

<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50">
        <!-- Tela de resultado com falha -->
        <div class="w-full max-w-4xl p-8 bg-white border-2 rounded-lg shadow-lg" :class="resultStyle.border">
            <div class="flex items-center gap-4 mb-6">
                <span class="text-xl font-semibold " :class="resultStyle.title">Carro com falha prevista</span>
            </div>
            <p class="text-center text-gray-700 text-xl font-medium mb-6">KNR: {{ knr }}</p>
            <div class="grid grid-cols-9 gap-4 mt-2">
                <template v-for="(failType, _index) in failTypes" :key="_index">
                    <div class="border-2 border-gray-30 rounded-lg px-10 py-10 mx-1"
                        :class="[styles[failType.status].bg, styles[failType.status].border]">
                        <p class="font-bold" :class="styles[failType.status].text">{{ failType.title }}</p>
                    </div>
                </template>
            </div>
            <!-- Botão de Voltar -->
            <button @click="voltar" class="mt-4 px-4 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600">
                Voltar
            </button>
        </div>
    </div>
</template>

<script setup>

import Axios from 'axios';


const knr = useRoute().params.knr;

const styles = {
    default: {
        border: 'border-gray-300',
        bg: '',
        title: 'text-gray-800',
        text: 'text-gray-800'
    },
    success: {
        border: 'border-green-400',
        bg: 'bg-green-500',
        title: 'text-green-600',
        text: 'text-white'
    },
    fail: {
        border: 'border-red-400',
        bg: 'bg-rose-500',
        title: 'text-red-600',
        text: 'text-white'
    }
};


const res = await Axios.get(`http://localhost:8000/api/predictions/details/${knr}`);

const failType = res.data.predicted_fail_codes;
console.log("Teste")
console.log(failType)
onMounted(() => {
    failTypes.value.forEach((fail) => {
        console.log(fail);
        failType.forEach((type) => {
            if (fail.failType === type) {
                fail.status = 'fail';
                if (result.value === 'success' || result.value === 'default') {
                    result.value = 'fail';
                }
            }
        });
    });
    if (result.value === 'default') {
        result.value = 'success';
    }
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

const voltar = () => {
    if (knr.value.trim()) {
        navigateTo(`/prediction`);
    }
};

</script>