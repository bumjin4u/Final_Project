<template>
  <div>
    <div class="d-flex justify-content-between">
      <span></span>
      <h1><b>게시글 수정</b></h1>
      <button type="button" class="btn btn-success m-2" @click="updateArticle">수정하기</button>
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
import SearchEngine from '@/components/SearchEngine.vue'
import MovieItem from '@/components/MovieItem.vue'

import axios from 'axios'
export default {
  name : 'ArticleUpdateView',
  components : {
    SearchEngine,
    MovieItem,
  },
  data : function(){
    return {
      article_id : this.$route.params.article_id,
      title : null,
      content : null,
      selectedMovie : null,
      movies : null,
    }
  },
  methods : {
    getArticleDetail(){
      axios({
        method : "GET",
        url : `http://127.0.0.1:8000/articles/${this.article_id}/`
      })
        .then((response)=>{
          this.title = response.data.title
          this.content = response.data.content
          this.selectedMovie = response.data.movie
        })
        .catch((error)=>{
          console.log(error)
        })
    },
    updateArticle(){
      axios({
        method : "PUT",
        url : `http://127.0.0.1:8000/articles/${this.article_id}/`,
        data : {
          title : this.title,
          content : this.content,
          movie : this.selectedMovie?.id
        },
        headers : {
          Authorization : `Token ${this.$store.state.Token}`
        }
      })
        .then(()=>{
          this.$router.push(`/articles/${this.article_id}`)
        })
        .catch((error)=>{
          console.log(error)
        })
    },
    saveMovies(data){
      this.movies = data
    },
    saveSelectedMovie(movie){
      this.selectedMovie = movie
    },
    selected(movie){
      return this.selectedMovie === movie
    },
  },
  created(){
    this.getArticleDetail()
  }
}
</script>

<style scoped>
.selected {
  border: 1px solid blue;
}
.none {
  opacity: 0.5;
}
</style>