import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

// 전역 네비게이션 가드
import { useCounterStore } from '@/stores/counter'

// const store = useCounterStore()
router.beforeEach((to, from ) => { // 메인 갈 때 마다
  // to : 다음 이동 경로
  // from : 현재 route
  const store = useCounterStore()
  // 밖에서 하면 에러
  if (to.name === 'ArticleView' && !store.isLogin ) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if (to.name === 'SignUpView' || to.name === 'LogInView' && (store.isLogin)) {
    window.alert('이미로그인햇읍니다람쥐썬더')
    return { name : 'ArticleView'}
  }
})

export default router
