<template>
  <div class="container article-list">
    <ul class="list-group">
      <ArticleListItem 
      v-for="article in articles" :key="article.id" :article="article"
      />
    </ul>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  data() {
    return {
      articles: null
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
      })
      .then((res) => {
        this.articles = res.data
      })
      .catch((err) => {
      console.log(err)
      })
    },
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
