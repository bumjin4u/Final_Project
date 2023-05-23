<template>
  <div>
    <h3>니코니코니~</h3>
    <MovieItem
    v-for="movie in movies" :key="movie.id"
    :movie="movie"
    />
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import MovieItem from '@/components/MovieItem.vue'
export default {
  name : "AnimationView",
  components : {
    MovieItem,
  },
  data : function(){
    return {
      movies : null
    }
  },
  methods : {
    getMovies : function(){
      axios({
        method : "GET",
        url : "http://127.0.0.1:8000/movies/animation"
      })
        .then((response)=>{
          this.movies = _.sampleSize(response.data,10)
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