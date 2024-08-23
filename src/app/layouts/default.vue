<template>
  <div class="flex flex-col min-h-screen">
    <header class="border-b-2 border-customBlue relative flex items-center p-4">
      <!-- Div na esquerda com a Logo e nome do projeto -->
    <div class="hover:scale-[101%] transition cursor-pointer flex items-center mr-12 ">
      <Logo width="w-12" class="mt-1"/>
      <p class="font-bold text-base">Cross The Line</p>
    </div>

    <!-- Div com os botões centralizados do header -->
    <div class="ml-12 absolute left-1/2 transform -translate-x-1/2 flex items-center gap-28">
      <HeaderButton iconName="mdi:chart-timeline-variant-shimmer" label="Previsão Diária" />
      <HeaderButton iconName="mdi:clipboard-text-outline" label="Histórico" />
      <HeaderButton iconName="mdi:view-dashboard-outline" label="Dashboard" />
      <HeaderButton iconName="mdi:progress-download" label="Treinamento Mensal" />
    </div>
  </header>

    <!-- Área com o conteúdo dá pagina -->
    <div class="flex-grow p-4 mb-16">
      <div class="min-h-[200vh]"> 
        <slot /> <!-- Conteúdo da página -->
      </div>
    </div>

    <!-- Footer da página -->
    <footer class="relative w-full bg-gray-800 text-white py-4 flex items-center justify-center">
      <p class="absolute left-1/2 transform -translate-x-1/2">&copy; 2024 Cross The Line. Todos direitos reservados.</p>
      <p class="ml-auto mr-2">Github</p>
      <a href="https://github.com/Inteli-College/2024-2A-T08-EC07-G01" target="_blank" class="ml-4">
        <Icon name="mdi:github" class="text-white text-2xl ml-auto mr-12 mt-1" />
      </a>
    </footer>
  </div>
</template>
