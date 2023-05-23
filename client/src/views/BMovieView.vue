<template>
  <div>
    <h1>B급 영화</h1>
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
    getBMovies : function(){
      axios({
        method : "GET",
        url : "http://127.0.0.1:8000/movies/Bmovie"
      })
        .then((response)=>{
          this.movies = response.data
        })
    }
  },
  created(){
    this.getBMovies()
  }
}
</script>

<style>

</style>