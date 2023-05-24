<template>
  <div>
    <div class="row g-1">
      <MovieItem
      v-for="movie in movies" :key="movie.id"
      :movie="movie"
      />
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
          const badwords = ['엄마','처제','젊은','욕망','신혼','서비스','이혼여행','새오빠','새누나','새언니','새색시','여사장','지스팟','스팟','스와핑','음란','과외','장모','동창회','섹스','이모','고모','외숙모', '형수', '여동생','오르가즘','며느리','젖','친구부부','외출 3','룸싸롱','언니','안마방','여대생','뜨거운 이웃','비뇨기과','여의사','맛 1','맛 2','맛 2016', '여직원의 맛']
          for (let badword of badwords){
            if (movie.title.includes(badword)){
              return false
            }
          }
          return true
        })
        this.movies = _.sampleSize(this.movies, 36)
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

<style scoped>
h1 {
  color: red;
}
</style>