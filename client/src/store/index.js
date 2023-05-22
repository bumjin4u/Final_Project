import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createdPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins : [
    createdPersistedState(),
  ],
  state: {
    articles: [
    ],
    Token : null,
    Username : null
  },
  getters: {
    isLogin(state) {
      return state.Token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, Token) {
      state.Token = Token
    },
    DELETE_TOKEN(state) {
      state.Token = null
    },
    SAVE_USERNAME(state, Username) {
      state.Username = Username
    },
    DELETE_USERNAME(state) {
      state.Username = null
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)

        })
        .catch((err) => {
        console.log(err)
        console.log('에러')
      })
    },
    signup(context, payload) {
      axios({
        method:'post',
        url: `${API_URL}/accounts/signup/`,
        data : {...payload},
      })
       .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        router.push({ name: 'ArticleView' })
        
       })
       .catch((err) => {
        console.log(err)
       })
    },
    login(context, payload) {
      axios({
        method:'post',
        url: `${API_URL}/accounts/login/`,
        data : {...payload},
      })
       .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        const account = JSON.parse(res.config.data)
        context.commit('SAVE_USERNAME', account.username)
        console.log(res)

        router.push({ name: 'ArticleView' })
        
       })
       .catch((err) => {
        console.log(err)
       })
    },
    logout(context) {
      context.commit('DELETE_TOKEN')
      context.commit('DELETE_USERNAME')
      alert('로그아웃 됐습니다!')
    },
  },
  modules: {
  }
})
