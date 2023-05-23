<template>
  <div v-if="movie" @click="goToDetail">
    <!-- 카드로 바꿀 것 -->
    <img :src="getImgURL(movie.poster_path)" alt="">
    <p>id : {{movie.id}}</p>
    <p>title : {{movie.title}}</p>
    <p>original_title : {{movie.original_title}}</p>
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
img {
  width: 100px;
  height: 100px;
}
</style>