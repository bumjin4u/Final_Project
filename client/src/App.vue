<template>
  <div id="app">
    <div class="homegrid">
      <nav class="navBar">
        <router-link class="btn" :to="{ name: 'MovieView'}">영화</router-link>
        <router-link class="btn" :to="{ name: 'ActorView'}">배우</router-link>
        <router-link class="btn" :to="{ name: 'ArticleView'}">게시물</router-link>
        <router-link class="btn" :to="{ name: 'SearchView'}">검색</router-link>
        <router-link class="btn" :to="{ name: 'RecommentdationView'}">추천</router-link>
        <router-link class="btn" v-if="!isLogin" :to="{ name: 'SignUpView'}">회원가입</router-link>
        <router-link class="btn" v-if="!isLogin" :to="{ name: 'LoginView'}">로그인</router-link>
        <router-link class="btn" v-if="isLogin" :to="{ name: 'ProfileView', params : { username : username}}">{{ username }}님</router-link>
        <a class="btn itemm" v-if="isLogin" @click="logout">로그아웃</a>
      </nav>
      <div class="view">
        <router-view/>
      </div>
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

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9));
  background-image: url('@/assets/blocks.jpg');
  color: white;
  height: 5300px;
}

.homegrid {
  display: grid;
  grid-template-columns: 100px auto;
  justify-content: center;
}
.navBar {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  border: 2px solid white;
  border-radius: 10px;
  height: 400px;
  margin-top : 120px;
  color : white;
  background-color: white;
}

.view {
  width: 1000px;
  margin-left : 60px;
  padding-top: 30px;
}
nav a.router-link-exact-active {
  color: #42b983;
}
</style>
