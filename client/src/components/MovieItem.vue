<template>
  <div @click="goToDetail">
    <!-- 카드로 바꿀 것 -->
    <p>id : {{movie.id}}</p>
    <p>title : {{movie.title}}</p>
    <p>original_title : {{movie.original_title}}</p>
    <p>poster_path : {{movie.poster_path}}</p>
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
      if (this.$router.history.current.path === '/articles/create'){
        this.$emit('selectMovie',this.movie)
      }
      else{
        this.$router.push(`/movies/${this.movie.id}`)
      }
    }
  }
}
</script>

<style>

</style>