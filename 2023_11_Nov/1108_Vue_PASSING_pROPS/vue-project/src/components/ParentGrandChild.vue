<template>
  <div>
    <p>parentGrandChild 에서 출력중{{ myMsg }}</p>
    <button @click="updateName"> 이름 변경 ! </button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String,
})

const emit = defineEmits(['updateName']) // emit 이벤트의 이름이다.
// 위에서 정의한 이름은 2번과 관련이 있다.
const updateName = function () { // 1. 여기는 그저 호출하기 위한 함수의 이름임. 굳이 다르게 할 이유가 없음
  emit('updateName')  // 2. 이것이 이름이다. 얘가 중요해요. 여기가 !!이벤트!!
}
</script>

<style  scoped>

</style>