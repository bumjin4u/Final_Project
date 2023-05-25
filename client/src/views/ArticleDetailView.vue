<template>
  <div>
    <h1>{{ article?.title }}</h1>
    <header> 
      <p>글 번호 : {{ article?.id }}</p>
      <a @click="goToProfile" style="cursor:pointer;">작성자 : {{ article?.username }}</a>
    </header>
    <section><p>{{ article?.content }}</p></section>
     
    <MovieItem 
    v-if="article"
    :movie="article.movie"
    />
    <br>
    <div class="info">
      <p>작성시간 : {{ article?.created_at.slice(0,10) }}</p>
      <p>수정시간 : {{ article?.updated_at.slice(0,10) }}</p>
      <p>추천수 : {{ article?.like_count }}</p>
    </div>
    <div class="btnBox" v-if="Author">
      <button v-if="Author" @click="goToArticleUpdate">수정</button>
      <br>
      <button v-if="Author" @click="deleteArticleDetail">삭제</button>
    </div>
    
    <div v-if="flag">
      <button class="btn btn-primary" type="button" @click="ArticleLike">좋아요 {{ article?.like_count }}</button>
      <!-- <p @click="ArticleLike" style="cursor:pointer;">&#10084;</p>
      <span>{{ article?.like_count }}</span> -->
    </div>
    <div v-else>
      <button class="btn btn-secondary" type="button" @click="ArticleLike">좋아요 {{ article?.like_count }}</button>
      <!-- <p @click="ArticleLike" style="cursor:pointer;">&#9825;</p>
      <span>{{ article?.like_count }}</span> -->
    </div>
    <CommentList 
    :article="article_id"
    />


  </div>
</template>


<script>
import axios from 'axios'
import MovieItem from '@/components/MovieItem.vue'
import CommentList from '@/components/CommentList.vue'


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieItem,
    CommentList,
  },
  data() {
    return {
      article: null,
      article_id : Number(this.$route.params.id),
      flag : false,
      Author : false
    }
  },
  created() {
    this.getArticleDetail(),
    this.checkUser()
  },
  computed: {
    Token() {
      return this.$store.state.Token
    },

  },
  methods: {
    getArticleDetail() {
      const article = this.article_id
      // console.log(article)
      axios({
        method: 'get',
        url: `${API_URL}/articles/${ article }/`,
      })
      .then((res) => {
        this.article = res.data
        this.Author = this.article.username === this.$store.state.Username
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToArticleUpdate() {
      this.$router.push(`/articles/${this.article_id}/update`)
    },
    deleteArticleDetail() {
      const Token = this.Token
      const article = this.article_id

      axios({
        method: 'delete',
        url: `${API_URL}/articles/${ article }/`,
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then(() => {
        this.$router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    ArticleLike() {
      const Token = this.Token
      const article = this.article_id

      axios({
        method: 'put',
        url: `${API_URL}/articles/${ article }/like/`,
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
    goToProfile() {
      if (this.$store.getters.isLogin){
        this.$router.push(`/profile/${this.article.username}`)
      }
      else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push('/login')
      }
    }
  }
}
</script>
<style scoped>
.info {
  display: flex;
  flex-direction: column;
  align-items: end;
}
header {
  display: flex;
  justify-content: space-between;
}
section {
  text-align: start;
  width: 1000px;
  height: 500px;
  background-color: white;
  color: black;
  border-radius: 5px;
  padding: 15px;
}
.btnBox {
  display: flex;
  justify-content: end;
}
</style>
