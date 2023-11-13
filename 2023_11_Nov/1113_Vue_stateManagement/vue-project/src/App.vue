<template>
  <div>
    <h1> Todo pjt</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount() }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
import { useCounterStore } from './stores/counter'; // 저장소 불러오기
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';
const store = useCounterStore()

</script>

<style  scoped>

</style>