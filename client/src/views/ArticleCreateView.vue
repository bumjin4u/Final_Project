<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <SearchEngine
      @getMovies="saveMovies"
      dynamic-props="movie"
      />
      <div v-if="movies" class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5 d-flex justify-content-start g-1">
        <MovieItem
        v-for="movie in movies" :key="movie.id"
        @selectMovie="saveSelectedMovie"
        :movie="movie"
        :class="{'Selected':selected(movie), 'none':!selected(movie)}"
        />
      </div>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import SearchEngine from '@/components/SearchEngine.vue'
import MovieItem from '@/components/MovieItem.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  components: {
    SearchEngine,
    MovieItem
  },
  data() {
    return {
      title: null,
      content: null,
      selectedMovie: null,
      movies : null,
    }
  },
  computed: {
    Token() {
      return this.$store.state.Token
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const movie = this.selectedMovie?.id
      const Token = this.Token

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        data: { title, content, movie },
        headers: {
          Authorization: `Token ${Token}`
        },
      })
      .then(() => {
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        if (err.response.status === 401){
          this.$router.push({name : 'LoginView'})
        }
        else{
          console.log(err)
        }
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
