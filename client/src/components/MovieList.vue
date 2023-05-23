<template>
  <div>
    <h1>MovieList</h1>
    <br>
    <div class="container">
      <div class="row row-cols-4 d-flex justify-content-around">
        <MovieItem
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'
import axios from 'axios'
import _ from 'lodash'

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
        this.movies = this.movies.filter((movie)=>{
          const badwords = ['엄마','처제','젊은','욕망','신혼','서비스','이혼여행','새오빠','새누나','새언니','새색시','여사장','지스팟','스팟','스와핑','음란','과외','장모','동창회','섹스','이모','고모','외숙모', '형수', '여동생']
          for (let badword of badwords){
            if (movie.title.includes(badword)){
              return false
            }
          }
          return true
        })
        this.movies = _.sampleSize(this.movies, 30)
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