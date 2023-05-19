<template>
  <div>
    <h3>Comment List</h3>
    <CommentListItem 
    v-for="comment in comments" :key="comment.id" :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  computed: {
    comments() {
      return this.$store.state.comments
    }
  }
}
</script>


