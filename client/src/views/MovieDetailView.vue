<template>
  
  <div v-if="movie" :style="{'background-image': `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)) ,url(${back_img_url})`}">
      <h1 v-if="movie.tagline" class="title animation">"{{movie.tagline}}"</h1>

      <div>
        <div class="info">
          <img class="poster" :src="poster_img_url" alt="" onload style="margin: 10px;">
          <div class="docs">
            <div>
              <h1>{{movie.title}}</h1>
              <span v-for="genre in movie.genres" :key="genre.id">{{genre.name}} </span>
              <p class="overview fadein">{{movie.overview}}</p>
            </div>
            <h5>⭐ {{ movie.vote_average }} ({{ movie.vote_count }} 명 참여)</h5>
          </div>
        </div>
        <div>
          <h1>| 예고편 |</h1>
          <iframe :src="trailer_url" frameborder="0" width="700" height="400"></iframe>
        </div>
      </div>

      <div class="credit">
        <h1>| 출연진 |</h1>
          <div class="row">
            <ActorItem
            v-for="actor in movie.actors" :key="actor.id"
            :actor="actor"
            />
          </div>
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
      flag : false
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
          this.$store.dispatch('changenow',this.movie.title)
          this.changeDanger()
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
    },
    changeDanger() {
      const bads = [80, 27, 9648, 53, 10752, 28]
      const badwords = ['엄마','처제','젊은','욕망','신혼','서비스','이혼여행','새오빠','새누나','새언니','새색시','여사장','지스팟','스팟','스와핑','음란','과외','장모','동창회','섹스','이모','고모','외숙모', '형수', '여동생','오르가즘','며느리','젖','친구부부','외출 3','룸싸롱','언니','안마방','여대생','뜨거운 이웃','비뇨기과','여의사','맛 1','맛 2','맛 2016', '여직원의 맛']
      for (let badword of badwords){
        if (this.movie.title.includes(badword)){
          this.$store.dispatch('changedanger',true)
          return
        }
      }

      for (let genre of this.movie.genres){
        if (bads.includes(genre.id)){
          this.$store.dispatch('changedanger',true)
          return
        }
      }
      this.$store.dispatch('changedanger',false)
    },
  },
  created() {
    this.getMovieDetail()
    this.getTrailerURL()
  },
}
</script>

<style scoped>

.animation {
  animation-name: bounce-in;
  animation-duration: 1s;
}
@keyframes bounce-in {
  0% {
    transform: scale(3);
    color: white;
  }

}
.poster {
  width: 300px;
  border-radius: 5%;
}
.info {
  display: flex;
}
.title{
  padding: 20px;
}
.overview {
  padding: 30px;
  text-align: left;
  border-radius: 1%;
  margin-right: 20px;
  margin-left: 10px;
  color: white;
}
.docs {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.credit {
  margin-top: 20px;
}
.fadein {
  overflow: hidden;
  animation: fadein 1s ease-in-out;
}

@keyframes fadein{
  0% {
    opacity: 0;
    transform: translateY(20px)
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
</style>
