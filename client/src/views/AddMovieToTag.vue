<!-- views/CreateView.vue -->

<template>
  <div>
    <h3>태그할 영화</h3>
    <p>영화를 검색 후 영화를 선택해주세요.</p>
    <button class="btn btn-success" @click="addMovie">추가</button>
    <SearchEngine
      @getMovies="saveMovies"
      dynamic-props="movie"
    />
    <div v-if="movies" class="row">
      <MovieItem
      v-for="movie in movies" :key="movie.id"
      @selectMovie="saveSelectedMovie"
      :movie="movie"
      :class="{'Selected':selected(movie), 'none':!selected(movie)}"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchEngine from '@/components/SearchEngine.vue'
import MovieItem from '@/components/MovieItem.vue'

export default {
  name: 'ArticleCreateView',
  components: {
    SearchEngine,
    MovieItem
  },
  data() {
    return {
      selectedMovie: null,
      movies : null,
      tag_id : this.$route.params.tag_id,
    }
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    addMovie(){
        if (!this.selectedMovie){
          alert("영화 선택 후 추가해주세요.")
          return
        }
        axios({
            method : "POST",
            url :`http://127.0.0.1:8000/tags/${this.tag_id}/`,
            data : {
                movie_id : this.selectedMovie.id
            },
            headers : {
                Authorization : `Token ${this.Token}`
            }
        })
          .then((response)=>{
            if (response.status === 201){
              this.$router.push(`/tags/${this.tag_id}`)
            }
            else if (response.status === 208){
              alert('이미 포함된 영화입니다.')
              return
            }
          })
          .catch((error)=>{
            console.log(error)
          })
    },
    saveMovies(movies){
        this.movies = movies
    },
    saveSelectedMovie(movie){
      this.selectedMovie = movie
    },
    selected(movie){
      return this.selectedMovie === movie
    }
  }
}
</script>

<style scoped>
.Selected {
  opacity: 1;
}
.none {
  opacity: 0.5;
}
</style>
