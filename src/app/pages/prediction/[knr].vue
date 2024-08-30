<!--TODO: Type component-->

<template>
    <div class="flex items-center flex-col content-center justify-center mt-10">
        <p class="font-bold text-5xl text-center mx-5 mt-10">Teste de rodagem indicado</p>
        <div class="border-2 border-gray-30 rounded-[16px] py-0 mx-auto my-10" :class="resultStyle.border">
            <div :class="resultStyle.bg" class="w-full rounded-t-[12px]">
                <p class="font-bold text-4xl text-center mx-5" :class="resultStyle.text">{{ resultText }}</p>
            </div>
            <p class="font-bold text-4xl text-center mx-5 my-10">KNR: {{ knr }}</p>
            <p class="bold text-2xl text-center mx-5 mt-10 mb-5">Falha prevista: </p>

            <div class="grid grid-cols-7 grid-flow-col my-5 mx-5">
                <template v-for="(failType, _index) in failTypes" :key="_index">
                    <div class="border-2 border-gray-30 rounded-lg px-10 py-10 mx-1"
                        :class="[styles[failType.status].bg, styles[failType.status].border]">
                        <p class="font-bold" :class="styles[failType.status].text">{{ failType.title }}</p>
                    </div>
                </template>

            </div>
        </div>
    </div>
</template>

<script setup>
import Axios from 'axios';

const knr = useRoute().params.knr;

const styles = {
    default: {
        border: 'border-gray-300',
        bg: 'bg-gray-300',
        text: 'text-white'
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
    console.log(knr);
    console.log(res);
    console.log(res.data.predicted_fail_code);
    console.log(failType);

    updateFailStatuses();
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

function delay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function updateFailStatuses() {
    for (const fail of failTypes.value) {
        if (fail.failType === failType) {
            fail.status = 'fail';
        } else {
            fail.status = 'success';
        }

        await delay(50);
    }
}

</script>
