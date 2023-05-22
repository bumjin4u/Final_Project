<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p @click="goProfile">{{ article.username }}</p>
    <p>{{ article.like_count }}</p>
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  methods: {
    goProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/user/${this.article.username}`,
        headers: {
          Authorization: `Token ${this.Token}`
        },
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'ProfileView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>
