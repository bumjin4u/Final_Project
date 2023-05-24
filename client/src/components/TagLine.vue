<template>
  <div v-if="tagline.tagline" @click="goToDetail">
    <h2>"{{ tagline.tagline }}"</h2>
  </div>
</template>

<script>
export default {
  name : "TagLine",
  props : {
    tagline : Object
  },
  methods : {
    goToDetail : function(){
      const currentPath = this.$router.history.current.path
      if (currentPath === '/articles/create' || currentPath.endsWith('update')){
        this.$emit('selectMovie',this.movie)
      }
      else{
        this.$router.push(`/movies/${this.tagline.id}`)
      }
    }
  }
}
</script>

<style>

</style>