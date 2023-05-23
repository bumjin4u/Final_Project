<template>
  <div v-if="actors">
    <h1>ActorList</h1>
    <br>
    <div class="container">
      <div class="row row-cols-4">
        <ActorItem 
        v-for="actor in actors" class="col" :key="actor.id"
        :actor="actor"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ActorItem from './ActorItem.vue'
import _ from 'lodash'

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
            this.actors = _.sampleSize(response.data, 50)
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