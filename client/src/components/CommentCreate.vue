<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <label>내용 : </label>
      <textarea cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentCreate',
  props: {
    article: Number
  },
  data() {
    return {
      content: null,
    }
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    createComment() {
      const content = this.content
      const Token = this.Token
      const article = this.article
      // console.log(article)

      if (!content) {
      alert('내용 입력해주세요')
      return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/${ article }/comments/`,
        data: { content },
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then(() => {
        this.$emit('getComments')
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
