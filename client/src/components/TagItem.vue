<template>
  <div>
    <h2 class="tag" @click="goDetail" >#{{this.tag.name}}</h2>
  </div>
</template>

<script>
export default {
    name : "TagItem",
    props : {
      tag : Object
    },
    methods : {
      goDetail : function(){
        this.$router.push(`/tags/${this.tag.id}`)
      }
    }
}
</script>

<style scoped>
.tag {
  color : white
}
.tag:hover {
  text-decoration: underline;
}
</style>