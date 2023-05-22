<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <p>추천수 : {{ article?.like_count }}</p>
     
    <MovieItem 
    v-if="article"
    :movie="article.movie"
    />
    <br>

    <button @click="goToArticleUpdate">수정</button>
    <br>
    <button @click="deleteArticleDetail">삭제</button>
    

    <div v-if="flag">
      <button @click="ArticleLike">좋아요 해제</button>
    </div>
    <div v-else>
      <button @click="ArticleLike">좋아요</button>
    </div>
    <CommentList 
    :article="article_id"
    />

    <!--  -->
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
      flag : false
    }
  },
  created() {
    this.getArticleDetail(),
    this.checkUser()
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
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
    }
  }
}
</script>
