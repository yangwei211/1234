import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Testcase from '../views/Testcase.vue'

// 加载了VueRouter
Vue.use(VueRouter)

// 路由管理
const routes = [

  {
    // 指定路由
    path: '/',
    // 指定渲染哪个组件
    component: Home
  },
  {
    // 指定路由
    path: '/testcase',
    // 指定渲染哪个组件
    component: Testcase
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
