<template>
  <div v-if="this.profile">
    <h1>{{ profile?.username }}님의 프로필</h1>
    <div class="list-group">    
      <div class="list-group-item d-flex justify-content-around align-itmes-center">
        <p>팔로우 : {{ profile?.followings }}</p>
        <p>팔로워 : {{ profile?.followers_count }}</p>
      </div>
    </div>
    <h2>작성한 게시물</h2>
    <ol class="list-group" v-if="profile.articles">
      <ArticleListItem 
      v-for="article in profile.articles" :key="article.id" :article="article"
      />
    </ol>
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

    <h2>좋아요 누른 게시물</h2>

    <ol class="list-group" v-if="profile.like_articles">
      <ArticleListItem 
      v-for="article in profile.like_articles" :key="article.id" :article="article"
      />
    </ol>

    <button class="w-btn w-btn-indigo" type="button" v-if="checkMyPage()" @click="passwordChange">비밀번호변경</button>

    <div v-if="!checkMyPage()">
      <button v-if="checkFollow()" @click="Follow">팔로우 해제</button>
      <button v-if="!checkFollow()" @click="Follow">팔로우</button>
    </div>

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

#comment {
  display: flex; 
  justify-content: space-evenly;
  color: rgba(30, 174, 231);
  background-color: white;
  align-items: center;
  border: 1px solid black;
}

#like_article {
  display: flex; 
  justify-content: space-evenly;
  color: rgba(30, 174, 231);
  background-color: white;
  align-items: center;
  border: 1px solid black;
}

#follow {
  display: flex; 
  justify-content: space-evenly;
  color: rgba(30, 174, 231);
  background-color: white;
  align-items: center;
  border: 1px solid black;
}

#comment p {
  margin-bottom: 0px;
}

#like_article p {
  margin-bottom: 0px;
}
</style>