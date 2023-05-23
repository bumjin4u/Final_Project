<template>
  <div v-if="movie" @click="goToDetail" class="card" style="width: 18rem; padding-left: 0px; margin: 1em;">
    <!-- 카드로 바꿀 것 -->
    <img :src="getImgURL(movie.poster_path)" alt="" class="card-img-top">
    <div class="card-body">
      <p class="card-text">id : {{movie.id}}</p>
      <p class="card-text">title : {{movie.title}}</p>
      <p class="card-text">original_title : {{movie.original_title}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name : "MovieItem",
  props : {
    movie : Object
  },
  methods : {
    goToDetail : function(){
      const currentPath = this.$router.history.current.path
      if (currentPath === '/articles/create' || currentPath.endsWith('update')){
        this.$emit('selectMovie',this.movie)
      }
      else{
        this.$router.push(`/movies/${this.movie.id}`)
      }
    },
    getImgURL(path){
      return `https://image.tmdb.org/t/p/original${path}`
    }
  }
}
</script>

<style scoped>
.card-img-top {
  width: 18rem;
  height: 15rem;
  object-fit: cover;
}
</style>