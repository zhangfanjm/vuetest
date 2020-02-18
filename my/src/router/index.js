import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import User from '@/components/User'
import Home from '@/components/Home'
import Config from '@/components/Config'
import Application from '@/components/Application'
import Video from '@/components/Video'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: 'dist',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: Home
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
    {
      path: '/index',
      component: Home
    },
    {
      path: '/application',
      component: Application
    },{
      path: '/config',
      component: Config
    },
    {
      path: '/video',
      component: Video
    },
  ]
})
