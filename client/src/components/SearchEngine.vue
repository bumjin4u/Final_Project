<template>
  <div>
    <form @submit.prevent="search">
      <div v-if="dynamicProps === 'actor'">
        <label for="actor">배우 : </label>
        <input type="text" id="actor" v-model="actor"><br>

        <input type="submit" value="submit">
      </div>

      <div v-else>
        <label for="movie">영화 : </label>
        <input type="text" id="movie" v-model="movie"><br>

        <input type="submit" value="submit">
      </div>

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
      actor: null,
      movie: null,
    }
  },
  methods: {
    search() {
      if (this.actor != null) {
        const actor = this.actor
        axios({
          url : `http://127.0.0.1:8000/actors/search/actor/${actor}/`,
          method : 'get'
        })
          .then((response)=>{
            console.log(response.data)
          })
          .catch((error)=>{
            console.log(error)
          })
        this.actor = null
      }
      else {
        const movie = this.movie
        axios({
          url : `http://127.0.0.1:8000/movies/search/movie/${movie}/`,
          method : 'get'
        })
          .then((response)=>{
            console.log(response.data)
          })
          .catch((error)=>{
            console.log(error)
          })
        this.movie = null
      }
    }
  }
}
</script>

<style>

</style>