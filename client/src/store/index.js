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
    Token : null,
    Username : null
  },
  getters: {
    isLogin(state) {
      return state.Token ? true : false
    }
  },
  mutations: {
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
    signup(context, payload) {
      axios({
        method:'post',
        url: `${API_URL}/accounts/signup/`,
        data : {...payload},
      })
       .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        const account = JSON.parse(res.config.data)
        context.commit('SAVE_USERNAME', account.username)
        router.push({ name: 'ArticleView' })
        
       })
       .catch(() => {
        alert('이미 존재하는 아이디거나 비밀번호가 서로 다릅니다.')
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

        router.push({ name: 'ArticleView' })
        
       })
       .catch(() => {
        alert('아이디 혹은 비밀번호가 틀렸습니다.')
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
