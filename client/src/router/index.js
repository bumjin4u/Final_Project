import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleCreateView from '@/views/ArticleCreateView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import SearchView from '@/views/SearchView'
import MovieView from '@/views/MovieView'
import MovieDetailView from '@/views/MovieDetailView'
import ActorView from '@/views/ActorView'
import ActorDetailView from '@/views/ActorDetailView'
import ProfileView from '@/views/ProfileView'
import ArticleUpdateView from '@/views/ArticleUpdateView'
import PasswordChangeView from '@/views/PasswordChangeView'
import BMovieView from '@/views/BMovieView'
import SleepMovieView from '@/views/SleepMovieView'
import RecommendationView from '@/views/RecommendationView'
import TaglineView from '@/views/TaglineView'
import AnimationView from '@/views/AnimationView'
Vue.use(VueRouter)

const routes = [
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
  },
  {
    path: '/articles/create',
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
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/movies/:movie_id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/actors',
    name: 'ActorView',
    component: ActorView
  },
  {
    path: '/actors/:actor_id',
    name: 'ActorDetailView',
    component: ActorDetailView
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/articles/:article_id/update',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView
  },
  {
    path: '/profile/passwordchange',
    name: 'PasswordChangeView',
    component: PasswordChangeView
  },
  {
    path: '/recommendation',
    name: 'RecommentdationView',
    component: RecommendationView
  },
  {
    path: '/recommendation/B',
    name: 'BMovieView',
    component: BMovieView
  },
  {
    path: '/recommendation/sleep',
    name: 'SleepMovieView',
    component: SleepMovieView
  },
  {
    path: '/recommendation/tagline',
    name: 'TaglineView',
    component: TaglineView
  },
  {
    path: '/recommendation/isekai',
    name: 'AnimationView',
    component: AnimationView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior() { 
    return { x: 300, y: 0 } 
  },
  routes,
})

export default router
