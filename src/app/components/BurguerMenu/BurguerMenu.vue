<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';

const isMenuOpen = ref(false);
const menuRef = ref(null);
const buttonRef = ref(null);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const handleClickOutside = (event) => {
  if (
    menuRef.value && 
    !menuRef.value.contains(event.target) && 
    !buttonRef.value.contains(event.target)
  ) {
    isMenuOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside);
});

const lineBaseClass = 'block h-1 w-full bg-black transition-transform duration-300 ease-in-out';

const menuClass = computed(() =>
  `fixed top-0 left-0 h-full w-1/6 bg-gray-700 bg-opacity-50 transform ${
    isMenuOpen.value ? 'translate-x-0' : '-translate-x-full'
  } transition-transform duration-300 ease-in-out`
);
</script>


<template>
  <div>
    <button 
      @click="toggleMenu" 
      class="relative z-50 flex flex-col justify-between w-8 h-8 focus:outline-none"
      ref="buttonRef"
    >
      <span :class="`${lineBaseClass} ${isMenuOpen ? 'rotate-45 translate-y-2' : ''}`"></span>
      <span :class="`${lineBaseClass} ${isMenuOpen ? 'opacity-0' : ''}`"></span>
      <span :class="`${lineBaseClass} ${isMenuOpen ? '-rotate-45 -translate-y-2' : ''}`"></span>
    </button>

    <!-- Ainda falta colocar os links (falta fzr as outras páginas)-->
    <div :class="menuClass" ref="menuRef" @click.stop>
      <nav class="flex flex-col items-center space-y-10 mt-16">
        <Logo width="w-20" class="mt-6"/>
        <a href="/test" class="text-xl hover:text-gray-300 transition duration-300">Previsão Diária</a>
        <a href="#" class="text-xl hover:text-gray-300 transition duration-300">Histórico</a>
        <a href="#" class="text-xl hover:text-gray-300 transition duration-300">Dashboard</a>
        <a href="#" class="text-xl hover:text-gray-300 transition duration-300">Treinamento Mensal</a>
      </nav>
    </div>
  </div>
</template>

