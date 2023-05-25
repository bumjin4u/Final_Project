<template>
  <div>
    <div>
      <h1>#이거 어때?</h1>
      <button class="btn btn-primary" @click="showForm">#태그만들기</button>
      <div v-if="show" class="input-group my-3 wid">
        <span class="input-group-text" id="basic-addon1">#</span>
        <input type="text" class="form-control" placeholder="#을 제외하고 입력" v-model="name">
        <button class="btn btn-primary" type="button" @click="createTag">만들기</button>
      </div>
    </div>
    <br>
    <TagItem
      v-for="tag in tags" :key="tag.id"
      :tag="tag"
    />
  </div>
</template>

<script>
import TagItem from '@/components/TagItem.vue'
import axios from 'axios'
export default {
    name : "TagList",
    data : function(){
      return {
        tags : null,
        show : false,
        name : null,
      }
    }
    ,
    components : {
        TagItem,
    },
    methods : {
      getTags : function(){
        axios({
          method : "GET",
          url : 'http://127.0.0.1:8000/tags/'
        })
          .then((response)=>{
            this.tags = response.data
          })
          .catch((error)=>{
            console.log(error)
          })
      },
      showForm(){
        if (this.$store.getters.isLogin){
          this.show = !this.show
        }
        else {
          alert('로그인이 필요한 서비스입니다.')
        }
      },
      createTag : function(){
        if (!this.name){
          alert('태그를 입력해주세요.')
          return
        }
        axios({
          method : "POST",
          url : "http://127.0.0.1:8000/tags/",
          data : {
            name: this.name
          },
          headers : {
            Authorization : `Token ${this.$store.state.Token}`
          }
        })
          .then((response)=>{
            console.log(response)
            this.show = !this.show
            this.getTags()
          })
          .catch((error)=>{
            console.log(error)
          })
      },
    },
    created(){
      this.getTags()
      this.$store.dispatch('changenow','#이거어때')
    }
}
</script>

<style scoped>
.wid {
  width: 50%;
  margin-left: 250px;
}
</style>