<template>
  <transition name="bounce">
    <div v-if="taglines">
      <h1>미안하다 이거 보여주려고 어그로 끌었다...</h1>
      <TagLine
      v-for="tagline in taglines" :key="tagline.id"
      :tagline="tagline"
      />
    </div>
  </transition>
</template>

<script>
import _ from 'lodash'
import TagLine from '@/components/TagLine.vue'
import axios from 'axios'
export default {
  name : "TaglineView",
  components : {
    TagLine
  },
  data : function(){
    return {
      taglines : null
    }
  },
  methods : {
    getTaglines : function(){
      axios({
        method : "GET",
        url : "http://127.0.0.1:8000/movies/taglines"
      })
        .then((response)=>{
          this.taglines = _.sampleSize(response.data,40)
        })
    }
  },
  created(){
    this.getTaglines()
  }
}
</script>

<style>
.bounce-enter-active {
  /* transition: all .5s ease; */
  animation: bounce-in 2s;
}
.bounce-leave-active {
  /* animation: bounce-in .5s reverse; */
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(5);
  }
  100% {
    transform: scale(1);
  }
}
</style>