<template>
  <div>
    <p>이름 : {{ profile?.username }}</p>
    <p>팔로우 : {{ profile?.followings }}</p>
    <p>팔로워 : {{ profile?.followers }}</p>
    <p>작성한 게시물 : {{ profile?.articles }}</p>
    <p>작성한 댓글 : {{ profile?.comments }}</p>
    <p>좋아요 누른 댓글 : {{ profile?.like_articles }}</p>
    <p>팔로워 리스트 : {{profile?.followerlist}}</p>
    <a @click="passwordChange">비밀번호변경</a>

    <button @click="Follow">팔로우 해제</button>

    <button @click="Follow">팔로우</button>

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
      falg : false
    }
  },
  computed: {
    Username() {
      return this.$route.params.username
    },
    Token() {
      return this.$store.state.Token
    },
  },
  created() {
    this.getProfile()
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
        console.log(this.profile)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    Follow() {
      const Token = this.Token
      const userId = this.profile.id

      axios({
        method: 'post',
        url: `${API_URL}/user/${ userId }/follow/`,
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then((res) => {
        this.getProfile(),
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
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