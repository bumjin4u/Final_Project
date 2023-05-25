<template>
  <div id="app" :class="{'dangermode': dangermode, 'safemode': !dangermode}">
    <header @click="[reload, playsound()]" style="cursor:pointer;">
      <img v-if="!dangermode" class="fadein" src="@/assets/ldd6.png" alt="" @click="reload">
      <img v-if="dangermode" class="fadein" src="@/assets/plankton.png" alt="" @click="reload">
      <h1 class="title">{{this.$store.state.now}} 좋아~</h1>
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
        <router-link class="btn navItem" v-if="isLogin" :to="{ name: 'ProfileView', params : { username : username}}">내 정보</router-link>
        <a class="btn navItem" v-if="isLogin" @click="logout">로그아웃</a>
      </nav>
      <div class="view">
        <router-view/>
      </div>
    </div>
  </div>
</template>


<script>
import sound from '@/assets/Monday.mp3'

export default {
  name: 'App',
  computed: {
    isLogin: function() {
      return this.$store.getters.isLogin
    },
    username: function(){
      return this.$store.state.Username
    },
    dangermode : function(){
      return this.$store.state.danger
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    reload(){
      if (this.$route.path ==='/'){
        this.$router.go(0)
      }
      else{
        this.$router.push('/')
      }
    },
    playsound() {
      if (sound) {
        const audio = new Audio(sound)
        audio.muted = true
        audio.play()
        audio.muted = false
      }
    }
  }
}
</script>

<style scoped>
#app {
  font-family: 'LOTTERIACHAB',Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-attachment:fixed;
  color: white;
  min-height: 1500px;
  min-width: 1500px;
  background-repeat: no-repeat;
}
.dangermode {
  background-image : url('@/assets/rockbottm.jpg')
}
.safemode{
  background-image : url('@/assets/ConchStreetStock.png')
}

.homegrid {
  font-family: 'Cafe24Ssurround';
  display: grid;
  grid-template-columns: 100px auto;
  justify-content: center;
  color: antiquewhite;
}
.navBar {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  border: 2px solid white;
  border-radius: 10px;
  height: 400px;
  margin-top : 120px;
  position: sticky;
  top: 100px;
  background-color: white;
  color: skyblue;
}
.navItem {
  color: skyblue;
  font-size : 17px;
}

.view {
  width: 1000px;
  margin-left : 60px;
  padding-top: 30px;
}
nav a.router-link-exact-active {
  color: darkblue;
}
header {
  display: flex;
  justify-content: center;
  align-items: center;
  color : yellow;
  padding-top : 20px;
}
img {
  width: 100px;
  height: 100px;
}
.title {
  font-size: 60px;
  margin-left: 20px;
}
.fadein {
  font-size: medium;
  position: relative;
  overflow: hidden;
  animation: fadein 1s cubic-bezier(0.0, 0.0, 0.0 ,0.0);
  animation-iteration-count: infinite;
}
.fadein:hover {
  animation-play-state: paused;
}

@keyframes fadein{
  0% {
    overflow: hidden;
    transform: translateY(-30px);
  }
  50% {
    overflow: hidden;
    transform: translateY(0px);
  }
  100% {
    overflow: hidden;
    transform: translateY(-30px);
  }
}
@font-face{
    font-family: 'LOTTERIACHAB';
    src: url('@/font/chab.ttf');
    font-weight: normal;
    font-style: normal;
}
@font-face{
    font-family: 'LOTTERIADDAG';
    src: url('@/font/ddag.ttf');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'Cafe24Ssurround';
    src: url('@/font/Cafe.ttf');
    font-weight: normal;
    font-style: normal;
}
</style>
