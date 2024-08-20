<script setup>
import { defineProps } from 'vue';

// Define the width prop with a default value
const props = defineProps({
  width: {
    type: String,
    default: 'w-10', // Default width as a Tailwind CSS class
  },
});
</script>

<template>
  <div :class="[props.width, 'overflow-hidden', 'rounded-lg']">
    <img src="@/assets/static/logo.png" alt="logo" />
  </div>
</template>
