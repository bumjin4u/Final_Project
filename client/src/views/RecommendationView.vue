<template>
  <div>
    <nav>
      <router-link :to="{ name : 'SleepMovieView' }">#보다 주무세요</router-link> | 
      <router-link :to="{ name : 'BMovieView' }">#B급영화</router-link> | 
      <router-link :to="{ name : 'TaglineView' }">#미안하다이거보여주려고어그로끌었다 | </router-link>
      <router-link :to="{ name : 'AnimationView' }">#이세계로...</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name : "RecommentdationView",
  created(){
    this.$store.dispatch('changenow','추천')
  }
}
</script>

<style>

</style>