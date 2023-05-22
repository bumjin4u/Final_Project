<template>
  <div>
    <p>{{ comment.content }}</p>
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