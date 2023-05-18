<template>
  <div>
    <form @submit.prevent="search">
      <div v-if="dynamicProps === 'actor'">
        <label for="actor">배우 : </label>
        <input type="text" id="actor" v-model="actor"><br>

        <input type="submit" value="submit">
      </div>

      <div v-else>
        <label for="movie">영화 : </label>
        <input type="password" id="movie" v-model="movie"><br>

        <input type="submit" value="submit">
      </div>

    </form>
  </div>
</template>

<script>
export default {
  name: 'SearchEngine',
  props: {
    dynamicProps: String
  },
  data() {
    return {
      actor: null,
      movie: null,
    }
  },
  methods: {
    search() {
      if (this.actor != null) {
        const actor = this.actor
        const url = 'actor'
        const payload = { url, actor }
        this.$store.dispatch('search', payload)
      }
      else {
        const movie = this.movie
        const url = 'movie'
        const payload = { url, movie }
        this.$store.dispatch('search', payload)
      }
    }
  }
}
</script>

<style>

</style>