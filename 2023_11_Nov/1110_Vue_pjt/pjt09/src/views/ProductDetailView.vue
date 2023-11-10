<template>
  <div>
    <h1>Prod. Detail</h1>
    <div v-if="product" class="product-card">
      <img :src="product.image">
          <strong> {{ product.title }}</strong>
          <p> 가격 : ${{ product.price }}</p>
    </div>
    <div v-else>
      <strong>로딩중</strong>
    </div>

  </div>

</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router';

const route = useRoute()
const product = ref('')
const productId = route.params.productId
console.log(productId)

const storeURL = `https://fakestoreapi.com/products/${productId}`

axios.get(storeURL)
  .then((response) => {
    // console.log(response) // 확인용
    product.value = response.data
  })
  .catch((error)=> {
    console.log(error)
  })

</script>

<style  scoped>

</style>