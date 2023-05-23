<template>
  <div>
    <!-- <form action="" v-if="dynamicProps === 'actor'" @submit.prevent="searchActor">
        <label for="actor">배우 : </label>
        <input type="text" id="actor" v-model="actor">
        <input type="submit" value="submit">
    </form>

    <form v-if="dynamicProps === 'movie'" @submit.prevent="searchMovie">
      <label for="movie">영화 : </label>
      <input type="text" id="movie" v-model="movie">
      <input type="submit" value="submit">
    </form> -->
    <div class="input-group mb-3">
      <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="true">{{target}}</button>
      <ul class="dropdown-menu">
        <li class="dropdown-item" @click="setTarget('영화')">영화</li>
        <li class="dropdown-item" @click="setTarget('배우')">배우</li>
      </ul>
      <input type="text" class="form-control" aria-label="Text input with dropdown button" v-model="query" @keyup.enter="search">
      <button class="btn btn-outline-secondary" @click="search">검색</button>
    </div>
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
      query : null,
      target : '선택',
      data: null,
    }
  },
  methods: {
    setTarget(choice){
      this.target = choice
    },
    search(){
      if (this.target==='선택'){
        alert('항목을 골라주세요')
        return
      }
      if (!this.query){
        alert('검색어를 입력해주세요.')
        return
      }
      if (this.target==='영화'){
        this.searchMovie()
        return
      }
      else {
        this.searchActor()
        return
      }
    },
    searchActor() {
      axios({
        url : `http://127.0.0.1:8000/actors/search/actor/${this.query}/`,
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
      axios({
          url : `http://127.0.0.1:8000/movies/search/movie/${this.query}/`,
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

<style scoped>

</style>