import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CartView from '@/views/CartView.vue'
import productDetailView from '@/views/productDetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name: 'home',
      component : HomeView
    },
    {
      path : '/cart',
      name: 'cart',
      component : CartView
    },
    {
      path : '/:productId',
      name: 'productDetail',
      component : productDetailView
    },
    
  ]
})

export default router
