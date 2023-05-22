<template>
  <div>
    <p>{{ comment.content }}</p>
    <button v-if="flag" @click="deleteCommentItem">삭제</button>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
// import { userInfo } from 'os'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  data : function(){
    return {
      flag : false
    }
  },
  created(){
    this.checkUser()
  },
  methods: {
    deleteCommentItem() {
      const Token = this.Token
      const comment = this.comment.id

      axios({
        method: 'delete',
        url: `${API_URL}/articles/comments/${ comment }/`,
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then(() => {
        this.$emit('deleteComment')
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
        this.flag = response.data.comments.some((comment)=>{
          return comment.id===this.comment.id
        })
      })
    }
  }
}
</script>

<style>

</style>