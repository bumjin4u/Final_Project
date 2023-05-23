<template>
  <div id="app">
    <div class="row">
      <nav class="col-1 mt-5">
        <router-link class="btn mt-1" :to="{ name: 'MovieView'}">영화</router-link><br>
        <router-link class="btn mt-1" :to="{ name: 'ActorView'}">배우</router-link><br>
        <router-link class="btn mt-1" :to="{ name: 'ArticleView'}">게시물</router-link><br>
        <router-link class="btn mt-1" :to="{ name: 'SearchView'}">검색</router-link><br>
        <router-link class="btn mt-1" :to="{ name: 'RecommentdationView'}">추천</router-link><br>
        <router-link class="btn mt-1" v-if="!isLogin" :to="{ name: 'SignUpView'}">회원가입<br></router-link>
        <router-link class="btn mt-1" v-if="!isLogin" :to="{ name: 'LoginView'}">로그인<br></router-link>
        <router-link class="btn mt-1" v-if="isLogin" :to="{ name: 'ProfileView', params : { username : username}}">{{ username }}님<br></router-link>
        <a class="btn mt-1" v-if="isLogin" @click="logout">로그아웃</a><br>
      </nav>
      <router-view class="col-10 mb-5"/>
    </div>
    <footer class="fixed-bottom bg-dark text-white">
      master ahn, slave park
    </footer>
  </div>
</template>


<script>
export default {
  name: 'App',
  computed: {
    isLogin: function() {
      return this.$store.getters.isLogin
    },
    username: function(){
      return this.$store.state.Username
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    reload(){
      this.$router.go(0)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 50px;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.navBar {
  width: 300px;
}
</style>
