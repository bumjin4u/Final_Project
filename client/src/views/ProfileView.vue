<template>
  <div v-if="this.profile">
    <div>
      <h1>{{ profile?.username }}</h1>
      <div v-if="!checkMyPage()">
        <button class="btn btn-primary" v-if="checkFollow()" @click="Follow">팔로우</button>
        <button class="btn btn-secondary" v-if="!checkFollow()" @click="Follow">팔로우</button>
      </div>
      <br>
      <div class="d-flex justify-content-center">
        <div class="left">
          <h6>팔로우 &#127774;</h6>
          {{ profile?.followings }}
        </div>
        <div class="right">
          <h6>팔로워 &#127773;</h6>
          {{ profile?.followers_count }}
        </div>
      </div> 
    </div>   
    <br>
    <h2>작성한 게시물</h2>
    <ol class="list-group" v-if="profile.articles">
      <ArticleListItem 
      v-for="article in profile.articles" :key="article.id" :article="article"
      />
    </ol>
    <br>
    <h2>작성한 댓글</h2>

    <div class="list-group" v-if="profile.comments">
      <div v-for="comment in profile.comments" :key="comment.id" class="list-group-item">
        <div class="d-flex w-100 justify-content-between align-itmes-center">
          <span class="mb-1">NO. {{ comment.id }} </span>
          <div class="mb-1">{{ comment.content }} </div>
          <div @click="goToArticle(comment.article.id)" style="cursor:pointer;">| 게시물 | {{ comment.article.title }}</div>
        </div>
      </div>
    </div>
    <br>
    <h2>좋아요 누른 게시물</h2>

    <ol class="list-group" v-if="profile.like_articles">
      <ArticleListItem 
      v-for="article in profile.like_articles" :key="article.id" :article="article"
      />
    </ol>
    <br>
    <button class="btn btn-success" type="button" v-if="checkMyPage()" @click="passwordChange">비밀번호변경</button>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleListItem from '@/components/ArticleListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "ProFile",
  components: {
    ArticleListItem,
  },
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
    goToArticle(ID) {
      this.$router.push({name: 'ArticleDetailView',params: {id: ID}})
    }
  }
}
</script>

<style scoped>
.left {
  margin-right: 15px;
  font-size: 20px;
}
.right {
  margin-left: 15px;
  font-size: 20px;
}
</style>