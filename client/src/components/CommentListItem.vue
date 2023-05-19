<template>
  <div>
    <h5>{{ comment.id }}</h5>
    <p>{{ comment.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>