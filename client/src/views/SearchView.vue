<template>
  <div>
    <div @click="SearchActor">배우</div>
    <div @click="SearchMovie">영화</div>
    <SearchEngine 
    :dynamic-props="dynamicProps"
    />
  </div>
</template>

<script>
import SearchEngine from '@/components/SearchEngine.vue'

export default {
  name: 'SearchView',
  components: {
    SearchEngine,
  },
  data() {
    return {
      dynamicProps: null
    }
  },
  methods: {
    SearchActor() {
      this.dynamicProps = "actor"
      console.log('배우')
    },
    SearchMovie() {
      this.dynamicProps = "movie"
      console.log('영화')
    }
  }
}
</script>

<style>

</style>