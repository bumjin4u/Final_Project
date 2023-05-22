<template>
  <div>
     <h1>PasswordChange Page</h1>
    <form @submit.prevent="passwordchange">

      <label for="new_password1"> password : </label>
      <input type="password" id="new_password1" v-model="new_password1"><br>

      <label for="new_password2"> password confirmation : </label>
      <input type="password" id="new_password2" v-model="new_password2">
      
      <input type="submit" value="PasswordChange">
    </form>
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
    }
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    passwordchange() {
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
        this.$router.push({name: 'LoginView'})
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