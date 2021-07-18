import Vue from 'vue'
import VueRouter from 'vue-router'
import Testcase from '../views/Testcase.vue'
import Layout from '../views/Layout.vue'
import Task from '../views/Task.vue'

// 加载了VueRouter
Vue.use(VueRouter)

// 路由管理
const routes = [

  {
    // 指定路由
    path: '/',
    // 指定渲染哪个组件
    // component: Home
    // 指定重定向页面
    redirect: "/layout"
  },
  {
    path: "/layout",
    component: Layout,
    children:[
      {
        path: "testcase",
        name: "testcase",
        component: Testcase
      },
      {
        path: "task",
        name: "task",
        component: Task
      }
    ]
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
