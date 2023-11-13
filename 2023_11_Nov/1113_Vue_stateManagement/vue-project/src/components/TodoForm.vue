<template>
  <div>
    <form @submit.prevent="createTodo()" >
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue'
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const todoText = ref('')
// const formElem = ref(null)
const createTodo = function () {
  // 사용자 입력 머시깽이를 어떻게 전달할 것인가.!
  store.addTodo(todoText.value)
  todoText.value=''
}
// 삭제 일치하는 것 - 뭔가 설정

</script>

<style  scoped>

</style>