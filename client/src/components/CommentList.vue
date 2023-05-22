<template>
  <div>
    <div>
      <h1>댓글 작성</h1>
      <form @submit.prevent="createComment">
        <label>내용 : </label>
        <input cols="30" rows="10" v-model="content">
        <input type="submit" id="submit">
      </form>
    </div>
    <h3>Comment List</h3>
    <CommentListItem 
    v-for="comment in comments" :key="comment.id" :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  data() {
    return {
      comments: null,
      content: null
    }
  },
  props: {
    article: Number
  },
  created() {
    this.getComments()
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    getComments() {
      const article = this.article
      axios({
        method: 'get',
        url: `${API_URL}/articles/${ article }/comments/`,
      })
      .then((res) => {
        this.comments = res.data
        console.log(res)
      })
      .catch((err) => {
      console.log(err)
      })
    },
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
        this.getComments()
        this.content = null
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>


