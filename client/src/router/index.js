import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleCreateView from '@/views/ArticleCreateView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import SearchView from '@/views/SearchView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/article/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
  },
  {
    path: '/article/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
