<template>
  <div>
    <h1>게시글 작성</h1>
    <div class="cont">
      <form @submit.prevent = 'createArticle'>
        <input type="text" v-model.trim="title">
        <textarea v-model.trim=content></textarea >
        <input type="submit">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useCounterStore()
const title = ref('')
const content = ref('')

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value // key 는 django model table을 따라야 함
    }
  })
  .then((res) => {
    console.log(res)
    router.push( { name: 'ArticleView'})
  })
  .catch((err) => {
    console.log(err)
  })
  }



</script>

<style>

</style>
