<template>
  <div v-if="this.profile">
    <p>이름 : {{ profile?.username }}</p>
    <p>팔로우 : {{ profile?.followings }}</p>
    <p>팔로워 : {{ profile?.followers_count }}</p>
    <p>작성한 게시물 : {{ profile?.articles }}</p>
    <p>작성한 댓글 : {{ profile?.comments }}</p>
    <p>좋아요 누른 댓글 : {{ profile?.like_articles }}</p>
    <p>팔로워 리스트 : {{profile?.followerlist}}</p>
    <button class="w-btn w-btn-indigo" type="button" v-if="checkMyPage()" @click="passwordChange">비밀번호변경</button>

    <div v-if="!checkMyPage()">
      <button v-if="checkFollow()" @click="Follow">팔로우 해제</button>
      <button v-if="!checkFollow()" @click="Follow">팔로우</button>
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
      username : this.$route.params.username
    }
  },
  created() {
    this.getProfile(),
    this.$store.dispatch('changenow',this.username)
  },
  beforeRouteUpdate(to, from, next){
      this.username = to.params.username
      this.profile = this.getProfile()
      next()
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/user/${this.username}`,
        headers: {
          Authorization: `Token ${this.$store.state.Token}`
        },
      })
      .then((response) => {
        this.profile = response.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    Follow() {
      const userId = this.profile.id
      axios({
        method: 'post',
        url: `${API_URL}/user/${ userId }/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.Token}`
        },
      })
      .then(() => {
        this.getProfile()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    passwordChange() {
      this.$router.push({name: 'PasswordChangeView'})
    },
    checkFollow(){
      const username = this.$store.state.Username
      if (this.profile.followers){
        for (let follower of this.profile.followers){
          if (username === follower.username){
            return true
          }
        }
      }
      return false
    },
    checkMyPage(){
      const username = this.$store.state.Username
      return this.profile.username === username
    },
  }
}
</script>

<style>
.w-btn {
    position: relative;
    border: none;
    display: inline-block;
    padding: 10px 20px;
    border-radius: 15px;
    font-family: "paybooc-Light", sans-serif;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s;
}

.w-btn-outline {
    position: relative;
    padding: 10px 20px;
    border-radius: 15px;
    font-family: "paybooc-Light", sans-serif;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s;
}

.w-btn-indigo {
    background-color: aliceblue;
    color: #1e6b7b;
}

.w-btn-indigo-outline {
    border: 3px solid aliceblue;
    color: #1e6b7b;
}

.w-btn-indigo-outline:hover {
    color: #1e6b7b;
    background: aliceblue;
}
</style>