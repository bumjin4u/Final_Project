<template>
  <div>
    <div v-if="!updateMode">
      <p>{{ content }}</p>
      <button v-if="flag" @click="deleteCommentItem">삭제</button>
      <button v-if="flag" @click="changeMode">수정</button>
    </div>
    <div v-else>
      <input type="text" v-model="content">
      <button @click="updateComment">수정하기</button>
    </div>
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
      flag : false,
      updateMode : false,
      content : this.comment.content
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
    },
    changeMode(){
      this.updateMode = !this.updateMode
    },
    updateComment(){
      axios({
        method : "PUT",
        url : `http://127.0.0.1:8000/articles/comments/${this.comment.id}/`,
        data : {
          content : this.content
        },
        headers : {
          Authorization : `Token ${this.$store.state.Token}`
        }
      })
        .then(()=>{
          this.changeMode()
        })
    }
  }
}
</script>

<style>

</style>