<template>
  <div v-if="movie" @click="goToDetail" class="col" style="cursor:pointer;">
    <!-- 카드로 바꿀 것 -->
    <img :src="getImgURL(movie.poster_path)" alt="" class="">
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
      if (currentPath === '/articles/create' || currentPath.endsWith('update') || currentPath.endsWith('add')) {
        this.$emit('selectMovie',this.movie)
      }
      else{
        this.$router.push(`/movies/${this.movie.id}`)
      }
    },
    getImgURL(path){
      return `https://image.tmdb.org/t/p/original${path}`
    },
  }
}
</script>

<style scoped>
img {
  margin-top : 1rem;
  width: 300px;
  height: 400px;
  transition: .5s;
  border-radius: 3%;
}
img:hover {
  scale: 1.1;
}
</style>