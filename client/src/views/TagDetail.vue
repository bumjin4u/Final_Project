<template>
    <div v-if="tag">
        <h1 class="tag">#{{tag.name}}</h1>
        <button class="btn btn-primary" type="button" @click="goCreate">새로운 영화 추가</button>
        <div class="row">
            <MovieItem
                v-for="movie in movies" :key=movie.id
                :movie="movie"
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import MovieItem from '../components/MovieItem.vue'

export default {
    name : "TagDetail",
    components : {
        MovieItem
    },
    data : function(){
        return {
            tag_id : this.$route.params.tag_id,
            tag : null,
            movies : null,
        }
    },
    methods : {
        getDetail(){
            axios({
                method : "GET",
                url : `http://127.0.0.1:8000/tags/${this.tag_id}`
            })
              .then((response)=>{
                this.movies = response.data.movies
                this.tag = response.data
              })
              .catch((error)=>{
                console.log(error)
              })
        },
        goCreate(){
            if (this.$store.getters.isLogin){
                this.$router.push(`/tags/${this.tag_id}/add`)
            }
            else{
                alert('로그인이 필요한 서비스 입니다.')
                this.$router.push({name : 'LoginView'})
            }
        }
    },
    created(){
        this.getDetail()
    }
}
</script>

<style>
.tag {
  color : pink
}
</style>