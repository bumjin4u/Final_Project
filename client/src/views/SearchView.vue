<template>
  <div>
    <div @click="SearchActor">배우</div>
    <div @click="SearchMovie">영화</div>
    <SearchEngine 
    :dynamic-props="dynamicProps"
    @getActors="saveActors"
    @getMovies="saveMovies"
    />
    <div v-if="actors">
      <ActorItem
      v-for="actor in actors"  :key="actor.id"
      :actor="actor"
      />
    </div>
    <div v-if="movies">
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
    SearchActor() {
      this.dynamicProps = "actor"
    },
    SearchMovie() {
      this.dynamicProps = "movie"
    },
    saveActors(actors){
      this.movies = null
      this.actors = actors
    },
    saveMovies(movies){
      this.movies = movies
      this.actors = null
    },  
  }
}
</script>

<style>

</style>