<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <SearchEngine
      @child-to-parent="parentGetEvent"
      />
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import SearchEngine from '@/components/SearchEngine.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  components: {
    SearchEngine,
  },
  data() {
    return {
      title: null,
      content: null,
      movie: null,
    }
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const movie = this.movie
      const Token = this.Token

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        data: { title, content, movie },
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    parentGetEvent: function(inputData) {
      this.movie = inputData[0]['id']
      // console.log(inputData)
    }
  }
}
</script>

<style>

</style>
