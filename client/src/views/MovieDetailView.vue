<template>
  <div v-if="movie" class="body" :style="{'background-image':`url(${back_img_url})`}">
    <h1>{{movie.title}}</h1>
    <div>
      <h3>예고편</h3>
      <iframe :src="trailer_url" frameborder="2" width="400" height="300"></iframe>
    </div>
    <h2 v-if="movie.tagline">{{movie.tagline}}</h2>
    <h2>{{ movie.vote_average }} / {{ movie.vote_count }}</h2>
    <div>
      <img :src="poster_img_url" alt="" onload>
      <h3>줄거리</h3>
      <p>{{movie.overview}}</p>
    </div>
    <div>
      <h4>장르</h4>
      <span v-for="genre in movie.genres" :key="genre.id">{{genre.name}} </span>
    </div>
    <div>
      <h4>출연진</h4>
      <ActorItem
      v-for="actor in movie.actors" :key="actor.id"
      :actor="actor"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ActorItem from '../components/ActorItem.vue'

export default {
  name : "MovieDetail",
  components : {
    ActorItem
  },
  data : function(){
    return {
      movie_id : this.$route.params.movie_id,
      BASE_URL : 'http://127.0.0.1:8000',
      movie : null,
      poster_img_url : null,
      back_img_url : null,
      trailer_url : null,
    }
  },
  methods : {
    getMovieDetail(){
      axios({
        method : "GET",
        url : `${this.BASE_URL}/movies/${this.movie_id}`
      })
        .then((response)=>{
          this.movie = response.data
          this.poster_img_url = 'https://image.tmdb.org/t/p/original' + '/' + this.movie.poster_path
          this.back_img_url = 'https://image.tmdb.org/t/p/original' + '/' + this.movie.backdrop_path
        })
        .catch((error)=>{
          console.log(error)
        })
    },
    getTrailerURL(){
      axios({
        method : "GET",
        url : `https://api.themoviedb.org/3/movie/${this.movie_id}/videos?language=ko-KR`,
        headers : {
          "accept": "application/json",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWNmYWRjNTI2NjkwNzcxNDQ1YzU4YWY1NWVjMWU3ZCIsInN1YiI6IjYzZDMxODA2ZTcyZmU4MDBlOWU2YTU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QX0Tk_RtXEBQcwdsCVO__ZPTgJGmOBjTRlf2yPdXDUU"
        }
      })
        .then((response)=>{
          for (let info of response.data.results){
            if (info.type == "Trailer"){
              this.trailer_url = `https://www.youtube.com/embed/${info.key}`
              break
            }
          }
        })
    }
  },
  created(){
    this.getMovieDetail(),
    this.getTrailerURL()
  }
}
</script>

<style scoped>
img {
  width: 300px;
  height: 400px;
}
.body {
  background-size: 50% ;
  background-repeat:no-repeat;
}
</style>
