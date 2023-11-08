<template>
  <div>
    {{ myMsg }}
    <ParentGrandChild :my-msg="myMsg" 
    @update-name="updateName"
    />
    <p>{{ dynamicProps }}</p>
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// 1. 문자열 선언 방식
// defineProps(['myMsg'])
// 2. 객체 선언 방식
// myMsg : String, // 데이터 타입 유효성 검사가 진행된다.
// Prop 각 객체에 객체 먹이기 가능
defineProps({ 
  dynamicProps: String,
  myMsg : {
    type : String,
    required : true,
    validator (value) {
      const validValue = ['success','warning', 'danger']
      if (!validValue.includes(value)) {
        console.error('에러!')
      }
    }
  }
  // validator(value) {
  //   return['success','warning', 'danger'].includes(value)
  // } 
})

// props 데이터를 script에서 사용하려면
// const props = defineProps({
//   myMsg: String,
//   dynamicProps: String,
//   validator(value) {
//     return['success','warning', 'danger'].includes(value)
//   } // 해당 배열에 없는 것을 전달한다면, 유효성 검사에서 탈락한다. 
// })
// console.log(props)
// 부모에게서 받은 것을 자신의 자식에게 주려면 v-bind 해야 함 동적 바인딩 !

// 이벤트- emit
const emit = defineEmits(['someEvent', 'emitArgs','updateName']) // 이 이름으로 소리치겠읍니다.
const buttonClick = function () {
  emit('someEvent') // 소리친 내용
}

// 이벤트 인자 전달
const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

// 자식이 준 updateName을 올려주자
const updateName= function () {
  emit('updateName')
}
</script>

<style  scoped></style>
