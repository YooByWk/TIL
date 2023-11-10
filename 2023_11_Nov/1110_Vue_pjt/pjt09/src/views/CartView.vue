<template>
  <div>
    <h1>CartView</h1>
    <div v-if="!cartItems"> 
    <strong>장바구니에 상품이 없습니다.</strong></div>
    <div v-else class="product-list">
      <!-- {{cartItems }} -->
      <div v-for="cartItem in cartItems" class="product-card" :key="cartItem.id">
        <!-- {{ product }} -->
        <img :src="cartItem.image">
        <strong> {{ cartItem.title }}</strong>
        <p> 가격 : ${{ cartItem.price }}</p>
        <button @click="goDetail(cartItem)">상세 페이지로 이동!</button>
        <button @click="removeCart(cartItem)"> 장바구니에서 삭제</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRouter } from 'vue-router';
const router = useRouter()
const cartItems = ref(null)
cartItems.value = JSON.parse(localStorage.getItem('cart')) || []
console.log(cartItems.value)


const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const removeCart = (product) => {
  // localstorage에서 삭제 
  // 현재 caritems.value 에서 삭제
  // 1. 현재 localstorage에 저장된 데이터 가져오기
  const existingCart = JSON.parse(localStorage.getItem('cart'))
  
  // 2. 삭제할 아이템 index 검색
  const itemIdx = existingCart.findIndex((item) => item.id === product.id)
  console.log(itemIdx)
  // 3. 삭제
  // splice = itemidx 에서 1개를 삭제한다.
  existingCart.splice(itemIdx, 1)
  // 4. 삭제된 데이터를 기준으로 데이터를 반영
  localStorage.setItem('cart', JSON.stringify(existingCart))
  cartItems.value = existingCart
}
// const remo
</script>

<style  scoped>

</style>