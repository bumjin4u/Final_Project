<template>
  <div v-if="actor" class="body">
    <div class="profile">
      <img :src="profile_url" alt="">
      <div class="info">
        <h2>{{actor.name}}</h2>
        <span v-if="actor.birthday">{{actor.birthday}}</span>
        <span> ~ </span>
        <span v-if="actor.deathday">{{actor.deathday}}</span>
      </div>
    </div>
    <div class="row">
      <MovieItem
      v-for="movie in actor.movies" :key="movie.id"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieItem from '@/components/MovieItem.vue'

export default {
  name : "ActorDetailView",
  components : {
    MovieItem
  },
  data : function(){
      return {
          actor_id : this.$route.params.actor_id,
          actor : null,
          profile_url : null,
      }
  },
  methods : {
    getActorDetail(){
      axios({
          method : "GET",
          url : `http://127.0.0.1:8000/actors/${this.actor_id}`
      })
      .then((response)=>{
        this.actor = response.data
        this.profile_url = 'https://image.tmdb.org/t/p/original' + this.actor.profile_path
        this.$store.dispatch('changenow',this.actor.name)
      })
      .catch((error)=>{
        console.log(error)
      })
    }
  },
  created(){
    this.getActorDetail()
  }
}
</script>

<style scoped>
img {
  width: 300px;
  height: 400px;
  border-radius: 5%;
}
.profile {
  display: flex;
  padding: 20px;
}
.info {
  margin-left: 30px;
  margin-top: 60px;
}
.profile {
  background-image: url('@/assets/actorprofile.jpg');
  background-attachment: fixed;
  background-size: cover;
}
.yellow{
  color: black;
}
</style>