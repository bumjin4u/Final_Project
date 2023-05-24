<template>
  <div id="loginForm">
    <h1>LogIn Page</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1"><b>ID</b></span>
      <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model="username">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1"><b>PW</b></span>
      <input type="password" class="form-control" placeholder="Password" aria-label="Username" aria-describedby="basic-addon1" v-model="password">
    </div>
    <button class="btn btn-primary" type="button" @click="login">Login</button>
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

}
#basic-addon1{
  width: 50px;
}
.input-group{
  width: 500px;
}
</style>
