<template>
  <div v-if="profile_img_url" @click="goToDetail" class="card" style="width: 18.8rem;">
    <img :src="profile_img_url" alt="" class="card-img-top">
    <div class="card-body">
      <p class="card-text">{{actor.name}}</p>
    </div>

  </div>
</template>

<script>
export default {
    name : "ActorItem",
    props : {
      actor : Object
    },
    data : function(){
      return {
        profile_img_url : null
      }
    },
    methods : {
      getProfileURL : function(){
        this.profile_img_url = 'https://image.tmdb.org/t/p/original' + this.actor.profile_path
      },
      goToDetail: function(){
        this.$router.push(`/actors/${this.actor.id}`)
      }
    },
    created(){
      this.getProfileURL()
    }
}
</script>

<style scoped>
img {
  width: 300px;
  height: 400px;
}
</style>