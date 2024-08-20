<template>
    <div :class="menuClass">
      <nav class="flex flex-col items-center space-y-4 mt-16">
        <a href="#" class="text-2xl hover:text-gray-300 transition duration-300">Home</a>
        <a href="#" class="text-2xl hover:text-gray-300 transition duration-300">About</a>
        <a href="#" class="text-2xl hover:text-gray-300 transition duration-300">Services</a>
        <a href="#" class="text-2xl hover:text-gray-300 transition duration-300">Contact</a>
      </nav>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  
  defineProps({
    isOpen: {
      type: Boolean,
      default: false,
    },
  });
  
  const menuClass = computed(() =>
    `fixed inset-0 z-40 bg-gray-900 bg-opacity-95 transform ${
      isOpen ? 'translate-x-0' : 'translate-x-full'
    } transition-transform duration-300 ease-in-out`
  );
  </script>
  