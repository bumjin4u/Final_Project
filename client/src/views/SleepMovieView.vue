<template>
  <div class="row">
    <h1>롱 ~~~~~ 타임 노 씨....</h1>
    <MovieItem
    v-for="movie in movies" :key="movie.id"
    :movie="movie"
    />
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'
import axios from 'axios'
export default {
  name : "SleepMovieView",
  components : {
    MovieItem
  },
  data : function(){
    return {
      movies : null
    }
  },
  methods : {
    getSleepMovies : function(){
      axios({
        method : "GET",
        url : "http://127.0.0.1:8000/movies/SleepMovie"
      })
        .then((response)=>{
          this.movies = response.data
        })
    }
  },
  created(){
    this.getSleepMovies(),
    this.$store.dispatch('changenow','수면영화')
  }
}
</script>

<style>

</style>