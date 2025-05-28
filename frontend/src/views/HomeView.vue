<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Button } from '@/components/ui/button'
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from '@/components/ui/dropdown-menu'
import { Moon, Sun } from 'lucide-vue-next'
import { useColorMode } from '@vueuse/core';

const backendResponse = ref("")

// Pass { disableTransition: false } to enable transitions
const mode = useColorMode({
  disableTransition: false
})

onMounted(() => {
  console.log("HomeView :: Hello world 👋")
})

// A little function to test out a call to the backend
const handleSayHello = async () => {
  const response = await fetch(`${import.meta.env.VITE_API_URL}/api/hello`)
  const data = await response.json()
  if (data.message) {
    backendResponse.value = data.message
  } else {
    console.error(data)
  }
}

</script>
<template>
  <div class="p-12 w-full max-w-screen-sm mx-auto">
    <h1 class="text-2xl mb-8">Vue.js FastAPI TypeScript Starter Project Template</h1>
    <p class="mb-4">This is a simple project template for a Vue.js and FastAPI project, set up to be a monorepo.</p>
    <p class="mb-16">This template is intended to be used for prototypes that use generative AI models. Take a look at the README.md file for more information.</p>
    <Button variant="default" class="mb-8" @click="handleSayHello">Say hello to the backend</Button>
    <div v-if="backendResponse">
      <h2 class="mb-4">Backend response:</h2>
      <p class="font-mono text-sm text-muted-foreground">{{ backendResponse }}</p>
    </div>
  </div>
  <!-- Light / Dark Mode Toggle -->
  <DropdownMenu>
    <DropdownMenuTrigger as-child class="absolute top-4 right-4">
      <Button variant="outline">
        <Moon class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
        <Sun class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
        <span class="sr-only">Toggle theme</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end">
      <DropdownMenuItem @click="mode = 'light'">
        Light
      </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'dark'">
        Dark
      </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'auto'">
        System
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>

<style scoped lang="postcss">

</style>