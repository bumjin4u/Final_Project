<template>
  <div class="d-flex justify-content-between align-items-center">
    <h5>No. {{ article.id }}</h5>
    <h5 class="underline" @click="goToDetail" style="cursor:pointer;">{{ article.title }}</h5>
    <div>
      <h5 class="underline" @click="goProfile" style="cursor:pointer;">{{ article.username }}</h5>
      <h5>&#128077; {{ article.like_count }}</h5>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  methods: {
    goProfile() {
      if (this.$store.getters.isLogin){
        this.$router.push({name: 'ProfileView', params : {username : this.article.username}})
      }
      else{
        this.$router.push({name: 'LoginView'})
      }
    },
    goToDetail(){
      if (this.$store.getters.isLogin){
        this.$router.push({name: 'ArticleDetailView',params: {id: this.article.id }})
      }
      else{
        this.$router.push({name: 'LoginView'})
      }
    }
  }
}
</script>

<style scoped>
.underline:hover {
  text-decoration: underline;
}
</style>
