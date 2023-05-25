<template>
  <div id="loginForm">
    <h1 class="title">로그인</h1>
    <div class="form-floating mb-3">
      <input type="email" class="form-control" id="floatingInput" v-model="username">
      <label for="floatingInput">아이디</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" v-model="password">
      <label for="floatingPassword">비밀번호</label>
    </div>
    <button type="button" class="btn btn-primary" @click="login">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  },
  created(){
    this.$store.dispatch('changenow','로그인')
  },
}
</script>
<style scoped>
#loginForm{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 100px;
}
.title  {
  font-weight: bolder;
}
.btn {
  margin-top: 10px;
}
</style>
