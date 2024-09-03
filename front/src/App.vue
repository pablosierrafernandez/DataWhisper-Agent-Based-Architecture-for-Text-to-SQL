<script setup>


import HeaderComponent from './components/HeaderComponent.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
 <HeaderComponent/>
  <router-view/>
  <FooterComponent/>
</template>

<style scoped>

</style>
