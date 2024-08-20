<template>
    <button @click="toggleMenu" class="relative z-50 flex flex-col justify-between w-8 h-8 focus:outline-none">
      <span :class="`${lineBaseClass} ${isOpen ? 'rotate-45 translate-y-2' : ''}`"></span>
      <span :class="`${lineBaseClass} ${isOpen ? 'opacity-0' : ''}`"></span>
      <span :class="`${lineBaseClass} ${isOpen ? '-rotate-45 -translate-y-2' : ''}`"></span>
    </button>
  </template>
  
  <script setup>
  import { ref, computed, defineEmits } from 'vue';
  
  const emit = defineEmits(['toggle']);
  
  const isOpen = ref(false);
  
  const toggleMenu = () => {
    isOpen.value = !isOpen.value;
    emit('toggle', isOpen.value);
  };
  
  const lineBaseClass = 'block h-1 w-full bg-black transition-transform duration-300 ease-in-out';
  </script>
  