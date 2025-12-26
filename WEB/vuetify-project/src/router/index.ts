import { createRouter, createWebHistory } from 'vue-router'
import UserList from '@/pages/index.vue'
import UserDetail from '@/pages/users/user.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: UserList,
  },
  {
    path: '/users/:username',
    name: 'user-detail',
    component: UserDetail,
    props: true,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/pages/NotFound.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
