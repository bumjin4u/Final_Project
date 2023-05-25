<template>
  <div>
    <li v-if="!updateMode" class="list-group-item d-flex justify-content-between align-items-start comment">
      <div class="ms-2 me-auto">
        <div class="fw-bold">{{ comment.username }}</div>
        {{content}}
      </div>
      <div class="btnBox" v-if="flag">
        <a @click="changeMode">수정 |</a>
        <a @click="deleteCommentItem">| 삭제</a>
      </div>
    </li>
    <li v-else class="list-group-item d-flex justify-content-between align-items-start comment">
      <div class="ms-2 me-auto">
        <div class="fw-bold">{{ comment.username }}</div>
        <div class="input-group">
          <input type="text" class="form-control" aria-describedby="button-addon2" v-model="content">
          <button class="btn btn-warning" type="button" id="button-addon2" @click="updateComment">수정</button>
        </div>  
      </div>
    </li>
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
    console.log(this.comment)
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

<style scoped>
.comment {
  display: flex;
  background-color : white;
  color: black;
  justify-content: space-between;
  border-bottom: 1px solid;
  border-radius: 5px;
  text-align: start;
}
.btnBox {
  display: flex;
  align-items: center;
  color: gray;
}
.username {
  font-size: 20px;
  color: rgb(30, 174, 231);
}
.content {
  font-size: 18px;
  color: rgb(30, 174, 231);
}
.time {
  font-size : 12px;
  color: gray;
}
.m3 {
  margin-left: 10px;
}
</style>