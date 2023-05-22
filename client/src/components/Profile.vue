<template>
  <div>
    <p>이름 : {{ profile?.username }}</p>
    <p>팔로우 : {{ profile?.followings }}</p>
    <p>팔로워 : {{ profile?.followers }}</p>
    <p>작성한 게시물 : {{ profile?.articles }}</p>
    <p>작성한 댓글 : {{ profile?.comments }}</p>
    <p>좋아요 누른 댓글 : {{ profile?.like_articles }}</p>
    <a @click="passwordChange">비밀번호변경</a>
    <div v-if="flag">
      <button @click="Follow">팔로우 해제</button>
    </div>
    <div v-else>
      <button @click="Follow">팔로우</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "ProFile",
  data() {
    return {
      profile: null,
      flag : false
    }
  },
  computed: {
    Username() {
      return this.$store.state.Username
    },
    Token() {
      return this.$store.state.Token
    },
  },
  created() {
    this.getProfile(),
    this.checkUser()
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/user/${this.Username}`,
        headers: {
          Authorization: `Token ${this.Token}`
        },
      })
      .then((res) => {
        // console.log(res)
        this.profile = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    Follow() {
      const Token = this.Token
      const userId = this.profile.id

      axios({
        method: 'put',
        url: `${API_URL}/user/${ userId }/follow/`,
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then(() => {
        this.getArticleDetail(),
        this.checkUser()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    checkUser() {
      const username = this.$store.state.Username
      if (!username ){
        return 
      }
      axios({
        method : "GET",
        url : `${API_URL}/user/${username}/`,
        headers : {
          Authorization : `Token ${this.Token}`
        }
      })
      .then((response)=>{
        this.flag = response.data.like_articles.some((like_article)=>{
          return like_article.id===this.article_id
        })
      })
    },
    passwordChange() {
      this.$router.push({name: 'PasswordChangeView'})
    }
  }
}
</script>

<style>

</style>