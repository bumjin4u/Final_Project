<template>
  <div>
    <nav class="m10">
      <router-link class="tags" :to="{ name : 'SleepMovieView' }">#보다 주무세요</router-link><br>
      <router-link class="tags" :to="{ name : 'BMovieView' }">#B급영화</router-link><br>
      <router-link class="tags" :to="{ name : 'TaglineView' }">#미안하다이거보여주려고어그로끌었다</router-link><br>
      <router-link class="tags" :to="{ name : 'AnimationView' }">#이세계로...</router-link>
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

<style scoped>
.tags {
  font-size: 50px;
  color: orange;
  margin-top: 30px;
}
.m10 {
  margin-top: 100px;
}
</style>