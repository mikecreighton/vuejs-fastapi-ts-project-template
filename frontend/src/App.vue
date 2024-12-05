<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const key = computed(() => route.fullPath)
</script>

<template>
  <RouterView :key="key" />
</template>

<style scoped lang="postcss">
</style>
