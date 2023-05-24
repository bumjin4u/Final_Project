<template>
  <div class="taglines">
    <h1>미안하다 이거 보여주려고 어그로 끌었다...</h1>
    <div v-if="taglines" class="rotate" >
      <div class="fadein">
        <TagLine
        v-for="tagline in taglines" :key="tagline.id"
        :tagline="tagline"/>
      </div>
      <!-- <TagLine
      v-for="tagline in taglines" :key="tagline.id" class="fadein" 
      :tagline="tagline" -->
      />
    </div>
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
        this.taglines = _.sampleSize(response.data,60)
        this.taglines = this.taglines.filter((tagline)=>{
          const badwords = ['엄마','처제','젊은','욕망','신혼','서비스','이혼여행','새오빠','새누나','새언니','새색시','여사장','지스팟','스팟','스와핑','음란','과외','장모','동창회','섹스','이모','고모','외숙모', '형수', '여동생','오르가즘','며느리','젖','친구부부','외출 3','룸싸롱','언니','안마방','여대생','뜨거운 이웃','비뇨기과','여의사','맛 1','맛 2','맛 3']
          for (let badword of badwords){
            if (tagline.tagline.includes(badword)){
              return false
            }
          }
          return true
        })
        if (this.taglines.length > 40){
          this.taglines = _.sampleSize(this.taglines,40)
        }
      })
    },
  },
  created(){
    this.getTaglines()
  },
}
</script>

<style>


.fadein {
  font-size: medium;
  position: relative;
  overflow: hidden;
  animation: fadein 45s cubic-bezier(0.0, 0.0, 0.0 ,0.0);
  animation-iteration-count: infinite;
}
.rotate {
  height: 70px;
  overflow: hidden;
}
.fadein:hover {
  animation-play-state: paused;
}

@keyframes fadein{
  0% {
    overflow: hidden;
    transform: translateY(70px);
  }
  100% {
    overflow: hidden;
    transform: translateY(-1500px);
  }
}
.taglines {
  height: 500px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>