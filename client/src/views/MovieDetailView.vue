<template>
  <div>
    <h1>{{movie.title}}</h1>
    <p>poster : {{movie.poster_path}}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name : "MovieDetail",
  data : function(){
    return {
      movie_id : this.$route.params.movie_id,
      BASE_URL : 'http://127.0.0.1:8000',
      movie : `...`,
    }
  },
  created(){
    axios({
      method : "GET",
      url : `${this.BASE_URL}/movies/${this.movie_id}`
    })
      .then((response)=>{
        this.movie = response.data
        console.log(this.movie)
      })
      .catch((error)=>{
        console.log(error)
      })
  }
}
</script>

<style>

</style>
