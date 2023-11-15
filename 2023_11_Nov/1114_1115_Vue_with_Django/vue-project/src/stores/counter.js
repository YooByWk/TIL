import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed (() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      // key header 달아주기
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res)=> {
      // console.log(res)
      articles.value = res.data
      console.log(articles.value)
    })
    .catch((err)=>  {
      console.log(err)
    })
  }
  
  const signup = function (payload) {
    // 구조분해할당
    const {username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        // username: payload.username,
        // password1: payload.password1,
        // password2: payload.password2
        username,
        password1,
        password2,
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logIn = function (payload) {
    // 입력 + 토큰 저장 해 줘야 함
    // 토큰이 이곳에 저장되어야 하는 이유는, 해당 토큰을 참조해야 하기 때문. 
    // 중앙 저장소를 이용 모든 곳에서 이용하기 위함
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
    })
    .then((res) => {
      console.log(res.data.key)
      token.value = res.data.key
      console.log(token.value)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  
  return { articles, API_URL, getArticles, signup, logIn, token, isLogin }
}, { persist: true })
