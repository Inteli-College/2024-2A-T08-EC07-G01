<template>
  <div class="flex flex-col min-h-screen">
    <!-- Header with logo -->
    <header class="w-full flex items-center gap-2 p-4 hover:scale-[101%] transition cursor-pointer">
      <Logo />
      <p class="font-bold">Cross The Line</p>
    </header>

    <!-- Main content area with added padding or height -->
    <div class="flex-grow p-4 mb-16">
      <div class="min-h-[200vh]"> <!-- Ensures enough space to require scrolling -->
        <slot /> <!-- Page content -->
      </div>
    </div>

    <!-- Footer at the bottom of the page -->
    <footer class="relative w-full bg-gray-800 text-white py-4 flex items-center justify-center">
      <p class="absolute left-1/2 transform -translate-x-1/2">&copy; 2024 Cross The Line. Todos direitos reservados.</p>
      <p class="ml-auto mr-2">Github</p>
      <a href="https://github.com/Inteli-College/2024-2A-T08-EC07-G01" target="_blank" class="ml-4">
        <Icon name="mdi:github" class="text-white text-2xl ml-auto mr-12 mt-1" />
      </a>
    </footer>
  </div>
</template>
