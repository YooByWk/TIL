<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }} 유저의 페이지입니다.</h2>
    <h2>user id : {{  userId }}</h2>
    <button @click="goHome">집으로</button>
    <button @click="goAnotherUser">100번 유저로</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute, onBeforeRouteLeave,onBeforeRouteUpdate } from 'vue-router';

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
// const userId =ref(router.params.id)
const goHome = function () {
  router.push( { name: 'home'})
}
//
// In-component Guard
// 1. 
onBeforeRouteLeave((to, from) => {
  const ans =  window.confirm('정말 떠나실건가요?')
  if  (ans === false) {
    return false
  }
})

// 2. onBeforeRouteUpdate
const goAnotherUser = function () {
  router.push({name : 'user', params : {id : 100}})
}
onBeforeRouteUpdate( (to,from) => {
  userId.value = to.params.id
})
</script>

<style  scoped>

</style>