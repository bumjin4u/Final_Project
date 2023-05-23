<template>
  <div>
    <h1>미안하다 이거 보여주려고 어그로 끌었다...</h1>
    <TagLine
    v-for="tagline in taglines" :key="tagline.id"
    :tagline="tagline"
    />
  </div>
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

</style>