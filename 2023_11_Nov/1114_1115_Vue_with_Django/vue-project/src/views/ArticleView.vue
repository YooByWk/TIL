<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{name: 'CreateView'}">[CREATE]</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';


const store = useCounterStore()

onMounted(()=> {
  store.getArticles() // 에러...
})
// 

</script>

<style>

</style>
