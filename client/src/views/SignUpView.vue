<template>
  <div id="signupForm">
    <h1 class='title'>회원가입</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">아이디</span>
      <input type="text" class="form-control" placeholder="아이디 ex) Sponge" v-model="username" @input="checkForm">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">비밀번호</span>
      <input type="password" class="form-control" placeholder="비밀번호" v-model="password1" @input="checkForm">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">비밀번호 확인</span>
      <input type="password" class="form-control" placeholder="비밀번호 확인" v-model="password2" @input="checkForm">
    </div>
    <span>{{errorMsg}}</span>
    <button class="btn btn-success" type="button" @click="signup">회원가입</button>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      errorMsg : null,
    }
  },
  computed : {
  },
  methods: {
    signup() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signup', payload)
    },
    checkForm(){
      if (!this.username){
        this.errorMsg = "아이디를 입력해주세요."
        return
      }
      if (!this.password1 || !this.password2){
        this.errorMsg = "비밀번호를 입력해주세요."
        return
      }
      if (this.password1 !== this.password2){
        this.errorMsg = "비밀번호가 서로 다릅니다."
        return
      }
      this.errorMsg = "성공"
    },
  },
  created(){
    this.$store.dispatch('changenow','회원가입')
  }
}
</script>
<style scoped>
#signupForm{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  margin-top: 100px;
}
#basic-addon1{
  width: 130px;
}
.input-group{
  width: 500px;
}
.title  {
  font-weight: bolder;
}
</style>
