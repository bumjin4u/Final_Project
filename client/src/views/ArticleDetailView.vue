<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>

    <MovieItem 
    v-if="article"
    :movie="article.movie"
    />
    <br>

    <!-- <button @click="updateArticleDetail">수정</button>
    <br> -->
    <button @click="deleteArticleDetail">삭제</button>

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
      const article = this.article_id
      // console.log(article)
      axios({
        method: 'get',
        url: `${API_URL}/articles/${ article }/`,
      })
      .then((res) => {
        this.article = res.data
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
        console.log('에러')
      })
    },
    // updateArticleDetail() {
    //   const article = this.article
    //   const title = this.title
    //   const content = this.content
    //   const movie = this.movie
    //   const Token = this.Token

    //   axios({
    //     method: 'put',
    //     url: `${API_URL}/articles/${ article.id }/`,
    //     data: { title, content, movie },
    //     headers: {
    //       Authorization: `Token ${Token}`
    //     },
    //   })
    //   .then(() => {
    //     this.$router.push({ name: 'ArticleView' })
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
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
    }
  }
}
</script>
