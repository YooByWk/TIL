<template>
  <div>
    <h1>home view</h1>
    <div v-if="productIsEmpty" class="product-list">
      <div v-for="product in products" class="product-card" :key="product.id">
        <!-- {{ product }} -->
        <img :src="product.image">
        <strong> {{ product.title }}</strong>
        <p> 가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세 페이지로 이동!</button>
        <button @click="addCart(product)"> 장바구니에 추가</button>
      </div>
    </div>
    <div v-else>
      <strong>로딩 중이거나, 상품 정보가 없습니다.</strong>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';

const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const products = ref([])
const router = useRouter()
const storeURL = 'https://fakestoreapi.com/products/'


axios.get(storeURL)
  .then((response) => {
    // console.log(response) // 확인용
    products.value = response.data
  })
  .catch((error)=> {
    console.log(error)
  })

const productIsEmpty = computed(() =>{
  return products.value.length > 0 ? true : false
  })

const addCart = (product) => {
  // localStorage.setItem('cart',JSON.stringify(product))
  // const tmp = localStorage.getItem('cart')
  // console.log(tmp)
  // Guarda solo 1 dato
  // chequea lo que repetido
  // 현재 로컬 스토리지에 저장된 데이터 가져오기
  // 없다면, 빈 리스트로 초기화
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []
  // si no hay length > 0, ocurre un error
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id )
  
  if(!isDuplicate) {
    alert('장바구니에 추가합니다.')
    existingCart.push(product)
  } else {
    alert('이미 있는 상품입니다. 장바구니로 이동합니다.')
  }
  // 수정된 카트 데이터를  localStorage 에 저장
  localStorage.setItem('cart',JSON.stringify(existingCart))
  // si no, anyadelo a la lista
  router.push('/cart')
  
}

</script>

<style  scoped>


</style>

<style>
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  /* text-align: center; */
}

.product-card {
  border: 1px solid;
  width: 205px;
  text-align: center;
}

.product-card img {
  width: 200px;
  height: 200px;
  object-fit: fill;
}
</style>