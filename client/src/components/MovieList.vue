<template>
  <div>
    MovieList
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
  name : "MovieList",
  data : function(){
    return {
      BASE_URL : "http://127.0.0.1:8000",
      movies : null,
    }
  },
  components : {
    MovieItem,
  },
  methods : {
    getMovies : function(){
      axios({
        method : "GET",
        url : `${this.BASE_URL}/movies/`
      })
       .then((response)=>{
        this.movies = response.data
       })
       .catch((error)=>{
        console.log(error)
       })
    }
  },
  created(){
    this.getMovies()
  }
}
</script>

<style>

</style>