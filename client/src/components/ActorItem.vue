<template>
  <div v-if="profile_img_url" @click="goToDetail" class="col detail" style="cursor:pointer;">
    <img class="banner_img" :src="profile_img_url" alt="">
    <p class="hover-text">프로필 보러 가기</p>
    <h3 class="pants">{{actor.name}}</h3>
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
  border-radius: 10px;
  transition: 0.5s;
}
.hover-text:hover{
  opacity: 1;
}
.img:hover{
  opacity: 0.5;
}
.hover-text{
  position: absolute;
  opacity: 0;
  width:87%;
  height:90%;
  top: 0px;
  left: 22px;
  padding-top: 170px;
}
.hover-text:hover{
  opacity: 1;
  transition: 0.5s;
}
</style>