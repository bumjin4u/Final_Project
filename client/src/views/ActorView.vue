<template>
  <div>
    <ActorList />
  </div>
</template>

<script>
import ActorList from '../components/ActorList.vue'

export default {
  name : "ActorView",
  components : {
    ActorList
  },
  created(){
    this.$store.dispatch('changenow','영화배우')
  }
}
</script>

<style>

</style>