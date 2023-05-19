<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'ArticleCreateView' }" @click="is_Logined">[CREATE]</router-link>
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
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    },
  is_Logined() {
    if (this.isLogin) {
      this.$router.push({ name: 'ArticleView' })
    }
    else {
      this.$router.push({ name: 'LoginView' })
    }
  }
  }
}
</script>

<style>

</style>
