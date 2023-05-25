<!-- views/CreateView.vue -->

<template>
  <div>
    <div class="d-flex justify-content-between">
      <span></span>
      <h1><b>게시글 작성</b></h1>
      <button type="button" class="btn btn-success m-2" @click="createArticle">작성하기</button>
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">제목</span>
      <input type="text" class="form-control" aria-describedby="basic-addon1" v-model="title">
    </div>

    <div class="input-group">
      <span class="input-group-text">내용</span>
      <textarea class="form-control" aria-label="With textarea" v-model="content" rows="10"></textarea>
    </div>
    <h3>태그할 영화</h3>
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
