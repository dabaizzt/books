import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { // 网站首页
      path: '/',
      name: 'Home',
      component: Home
    }
  ]
})
