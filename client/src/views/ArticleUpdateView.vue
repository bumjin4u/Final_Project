<template>
  <div>
    <h1>Article Update</h1>
    <label for="">제목 : </label>
    <input type="text" v-model="title"><br>
    <label for="">내용 : </label>
    <input type="text" v-model="content"><br>
    <SearchEngine
    @getMovies="saveMovies"
    dynamic-props="movie"
    />
    <div v-if="movies">
      <MovieItem
      v-for="movie in movies" :key="movie.id"
      @selectMovie="saveSelectedMovie"
      :movie="movie"
      :class="{'selected':selected(movie)}"
      />
    </div>
    <input type="submit" @click="updateArticle">
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
</style>