<template>
  <div class="container">
    <nav>
      <RouterLink to="/"> Home</RouterLink>
      <!-- <RouterLink to="/detail"> detail</RouterLink> -->
      <RouterLink to="/cart"> cart</RouterLink>
    </nav>
  </div>
  <div>
    <h1>app</h1>
    
  </div>
  <RouterView/>

</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';
</script>

<style  scoped>
.container {
  width:90%;
  margin: 0 auto;
}
</style>