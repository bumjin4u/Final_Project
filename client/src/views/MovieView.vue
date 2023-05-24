<template>
  <div>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name : "MovieView",
  components : {
    MovieList,
  },
  created(){
    this.$store.dispatch('changenow','영화')
  }
}
</script>

<style>

</style>