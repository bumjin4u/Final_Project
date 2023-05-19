<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.user }}</p>
    <p>{{ article.username }}</p>
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
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
