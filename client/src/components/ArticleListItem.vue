<template>
  <li class="list-group-item d-flex justify-content-between align-items-center">
    <span>No. {{ article.id }}</span>
    <span class="underline" @click="goToDetail">{{ article.title }}</span>
    <span class="badge bg-primary rounded-pill fs-5">&#128077; {{ article.like_count }}</span>
  </li>
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
