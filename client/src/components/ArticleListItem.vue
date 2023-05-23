<template>
  <div class="d-flex justify-content-between align-items-center">
    <h5>No. {{ article.id }}</h5>
    <h5 class="underline" @click="goToDetail">{{ article.title }}</h5>
    <div>
      <h5 class="underline" @click="goProfile">{{ article.username }}</h5>
      <h5>좋아요 : {{ article.like_count }}</h5>
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
      this.$router.push({name: 'ProfileView', params : {username : this.article.username}})
    },
    goToDetail(){
      this.$router.push({name: 'ArticleDetailView',params: {id: this.article.id }})
    }
  }
}
</script>

<style scoped>
.underline:hover {
  text-decoration: underline;
}
</style>
