<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <p>영화 : {{ article?.movie.id }}</p>
    <img v-if="article" :src="'https://image.tmdb.org/t/p/original'+article.movie.poster_path" alt="" width="300" height="400">
    <br>

    <button @click="updateArticleDetail">수정</button>

    <CommentList />
  </div>
</template>


<script>
import axios from 'axios'
import CommentList from '@/components/CommentList.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    CommentList
  },
  data() {
    return {
      article: null,
      updateMode: false

    }
  },
  created() {
    this.getArticleDetail()
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateArticleDetail() {
      const title = this.title
      const content = this.content
      const movie = this.movie
      const Token = this.Token

      axios({
        method: 'put',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
        data: { title, content, movie },
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
