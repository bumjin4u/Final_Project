<template>
  <div>
    <h1>PasswordChange Page</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">변경할 비밀번호</span>
      <input type="password" class="form-control" placeholder="비밀번호" aria-describedby="basic-addon1" v-model="new_password1" @input="checkForm">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">변경할 비밀번호 확인</span>
      <input type="password" class="form-control" placeholder="비밀번호 확인" aria-describedby="basic-addon1" v-model="new_password2" @input="checkForm">
    </div>
    <span class="error">{{ errorMsg }}</span>
    <button class="btn btn-success" type="button" @click="passwordchange">변경하기</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PasswordChangeView',
  data() {
    return {
      new_password1: null,
      new_password2: null,
      errorMsg : null,
    }
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    passwordchange() {
      if (!this.checkForm()){
        alert("아래 규칙을 지켜주세요.")
        return
      }
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        data: {
          new_password1, new_password2
        },
        headers: {
          Authorization: `Token ${this.Token}`
        },
      })
      .then(() => {
        this.$router.push('/')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    checkForm(){
      if (!this.new_password1 || !this.new_password2){
        this.errorMsg = "비밀번호를 입력해주세요."
        return false
      }
      else if (this.new_password1 !== this.new_password2){
        this.errorMsg = "비밀번호가 서로 다릅니다."
        return false
      }
      this.errorMsg = null
      return true
    }
  },
  created(){
    this.$store.dispatch('changenow','비밀번호 변경')
  }
}
</script>

<style scoped>
.error {
  color: red;
  font-size: 20px;
}
</style>