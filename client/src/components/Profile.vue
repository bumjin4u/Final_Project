<template>
  <div>
    <p>이름 : {{ profile?.username }}</p>
    <p>팔로우 : {{ profile?.followings }}</p>
    <p>팔로워 : {{ profile?.followers }}</p>
    <p>작성한 게시물 : {{ profile?.articles }}</p>
    <p>작성한 댓글 : {{ profile?.comments }}</p>
    <p>좋아요 누른 댓글 : {{ profile?.like_articles }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "ProFile",
  data() {
    return {
      profile: null
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
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>