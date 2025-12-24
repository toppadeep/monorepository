import { createRouter, createWebHistory } from "vue-router";
import UserList from '@/pages/index.vue'
import UserDetail from '@/pages/users/[id].vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: UserList,
    },
    {
        path: '/users/:id',
        name: 'user-detail',
        component: UserDetail,
        props: true,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    strict: true
})

export default router