<template>
  <div>
    <h1>커뮤니티</h1>
    <a class="btn btn-outline-light" @click="is_Logined">글 작성</a>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    is_Logined() {
      if (this.isLogin) {
        this.$router.push({ name: 'ArticleCreateView' })
      }
      else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({ name: 'LoginView' })
      }
    }
  },
  created(){
    this.$store.dispatch('changenow','커뮤니티')
  }
}
</script>

<style scoped>

</style>
