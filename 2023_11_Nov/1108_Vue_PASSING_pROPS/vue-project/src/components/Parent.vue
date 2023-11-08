<template>
  <div>
    <ParentChild 
    my-msg="qqqq" 
    :dynamic-props="name" 
    @some-event="someCallback"
    @emit-args="getNumbers"
    @update-name="updateName"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'
const name = ref('Alice') // 동적 props
const someCallback = function () {
  console.log('ParentChild가 발신한 emit 이벤트를 수신했습니다.')
}
const getNumbers = function (...args) {
  console.log(args)
}

const updateName =function () {
  if (name.value === 'Alice') {
    name.value = 'Bella'
  } else {
    name.value = 'Alice'
  }
  console.log('이름 변경 완료 :', name.value )
}
</script>

<style  scoped></style>