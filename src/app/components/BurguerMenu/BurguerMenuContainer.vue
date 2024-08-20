<!-- Não acabei ainda, só Deus sabe como isso funciona -->
<!-- A descobrir --> 

<script setup>
import { ref } from 'vue';

const isMenuOpen = ref(false);

const handleToggle = (isOpen) => {
  isMenuOpen.value = isOpen;
};
</script>

<template>
    <div>
      <BurgerButton @toggle="handleToggle" />
      <BurgerMenu :isOpen="isMenuOpen" />
    </div>
  </template>