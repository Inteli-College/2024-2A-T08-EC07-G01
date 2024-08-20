<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  width: {
    type: String,
    default: 'w-10', 
  },
});
</script>

<template>
  <div :class="[props.width, 'overflow-hidden', 'rounded-lg']">
    <img src="@/assets/static/logo.png" alt="logo" />
  </div>
</template>
