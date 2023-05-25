<template>
  <div>
    <nav class="m10">
      <router-link class="tags" :to="{ name : 'TaglineView' }"><h1>영화 맞추기</h1></router-link><br>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name : "RecommentdationView",
  created(){
    this.$store.dispatch('changenow','게임')
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