<template>
  <div>
    <form action="" v-if="dynamicProps === 'actor'" @submit.prevent="searchActor">
        <label for="actor">배우 : </label>
        <input type="text" id="actor" v-model="actor">
        <input type="submit" value="submit">
    </form>

    <form v-if="dynamicProps === 'movie'" @submit.prevent="searchMovie">
      <label for="movie">영화 : </label>
      <input type="text" id="movie" v-model="movie">
      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SearchEngine',
  props: {
    dynamicProps: String
  },
  data() {
    return {
      actor: '',
      movie: '',
      data: null,
    }
  },
  methods: {
    searchActor() {
      if (!this.actor){
        alert("입력 후 검색해주세요.")
        return
      }
      axios({
        url : `http://127.0.0.1:8000/actors/search/actor/${this.actor}/`,
        method : 'GET'
      })
        .then((response)=>{
          this.data = response.data
          this.$emit('getActors', this.data)
        })
        .catch((error)=>{
          console.log(error)
        })
    },
    searchMovie(){
      if (!this.movie){
        alert("입력 후 검색해주세요.")
        return
      }
      axios({
          url : `http://127.0.0.1:8000/movies/search/movie/${this.movie}/`,
          method : 'GET'
        })
          .then((response)=>{
            this.data = response.data
            this.$emit('getMovies', this.data)
          })
          .catch((error)=>{
            console.log(error)
          })
    },
  },
}
</script>

<style>

</style>