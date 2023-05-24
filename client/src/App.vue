<template>
  <div id="app">
    <header>
      <h1><b>🐯FLEX</b></h1>
    </header>
    <div class="homegrid">
      <nav class="navBar">
        <router-link class="btn navItem" :to="{ name: 'MovieView'}">영화</router-link>
        <router-link class="btn navItem" :to="{ name: 'ActorView'}">배우</router-link>
        <router-link class="btn navItem" :to="{ name: 'ArticleView'}">게시물</router-link>
        <router-link class="btn navItem" :to="{ name: 'SearchView'}">검색</router-link>
        <router-link class="btn navItem" :to="{ name: 'RecommentdationView'}">추천</router-link>
        <router-link class="btn navItem" v-if="!isLogin" :to="{ name: 'SignUpView'}">회원가입</router-link>
        <router-link class="btn navItem" v-if="!isLogin" :to="{ name: 'LoginView'}">로그인</router-link>
        <router-link class="btn navItem" v-if="isLogin" :to="{ name: 'ProfileView', params : { username : username}}">{{ username }}님</router-link>
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
  background-image: '@/assets/block2.jpg';
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
}
.navItem {
  color: white;
}

.view {
  width: 1000px;
  margin-left : 60px;
  padding-top: 30px;
}
nav a.router-link-exact-active {
  color: red;
}
header {
  color : red;
  padding-top : 20px;
}
</style>
