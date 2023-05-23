<template>
  <div v-if="profile_img_url" @click="goToDetail" class="card" style="width: 18rem; padding-left: 0px; margin: 1em;">
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

.card-img-top {
  width: 18rem;
  height: 15rem;
  object-fit: cover;
}
</style>