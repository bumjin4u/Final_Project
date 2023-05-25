<template>
  <div class="body">
    <SearchEngine 
    :dynamic-props="dynamicProps"
    @getActors="saveActors"
    @getMovies="saveMovies"
    />
    <div v-if="actors" class="row">
      <ActorItem
      v-for="actor in actors"  :key="actor.id"
      :actor="actor"
      />
    </div>
    <div v-if="movies" class="row">
      <MovieItem
      v-for="movie in movies" :key="movie.id"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import SearchEngine from '@/components/SearchEngine.vue'
import MovieItem from '@/components/MovieItem.vue'
import ActorItem from '@/components/ActorItem.vue'

export default {
  name: 'SearchView',
  components: {
    SearchEngine,
    MovieItem,
    ActorItem
  },
  data() {
    return {
      dynamicProps: null,
      movies : null,
      actors : null,
    }
  },
  methods: {
    saveActors(actors){
      this.movies = null
      this.actors = actors
    },
    saveMovies(movies){
      this.movies = movies
      this.actors = null
    },  
  },
  created(){
    this.$store.dispatch('changenow','검색')
  }
}
</script>

<style scoped>
</style>