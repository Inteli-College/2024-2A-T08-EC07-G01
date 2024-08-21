<script setup>
definePageMeta({
  layout: 'empty' 
});

</script>

<template>
  <div class="relative flex flex-col justify-center items-center h-screen space-y-20">

    <BurguerMenu class="absolute top-4 left-4" />    

    <Logo width="w-80" />
    
    <!-- Container com botões -->
    <div class="relative border border-gray-800 rounded-lg bg-gray-200 w-[300px] pt-10">
      <h1 class="absolute -top-5 left-1/2 transform -translate-x-1/2 px-2 bg-gray-200 text-3xl font-bold">
        Análise
      </h1>

      <div class="flex flex-col space-y-4 p-8">
        <Button class="w-full h-20 bg-gray-300">Histórico</Button>
        <Button class="w-full h-20 bg-gray-300">Dashboard</Button>
      </div>

      <Button class="absolute -left-40 top-1/2 transform -translate-y-1/2">
        Previsão Diária
      </Button>
      <Button class="absolute -right-48 top-1/2 transform -translate-y-1/2">
        Treinamento Mensal
      </Button>
    </div>
  </div>
</template>

