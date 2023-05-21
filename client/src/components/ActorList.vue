<template>
  <div v-if="actors">
    ActorList
    <ActorItem 
    v-for="actor in actors" :key="actor.id"
    :actor="actor"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ActorItem from './ActorItem.vue'

export default {
    name : "ActorList",
    components: {
      ActorItem
    },
    data : function(){
      return {
        actors : null
      }
    },
    methods : {
      getActors : function(){
        axios({
          method : "GET",
          url : 'http://127.0.0.1:8000/actors/'
        })
          .then((response)=>{
            this.actors = response.data.slice(0,30)
          })
          .catch((error)=>{
            console.log(error)
          })
      }
    },
    created(){
      this.getActors()
    }
}
</script>

<style>

</style>