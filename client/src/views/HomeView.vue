<template>
  <div>
    <h1>Home Sweet Home</h1>
    <div>
      <h1>{{ampm}} : {{hour}} : {{minutes}} : {{seconds}}</h1>
    </div>
  </div>
</template>

<script>
export default {
    name : "HomeView",
    data : function(){
      return {
        weekday : ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"],
        ampm : null,
        hour : null,
        minutes : null,
        seconds : null,
        day : null,
      }
    },
    methods : {
      getTime : function(){
        const date = new Date()
        const hour = date.getHours()
        const minutes = date.getMinutes()
        const seconds = date.getSeconds()
        this.day = date.getDay()
        this.hour = hour
        if (hour > 12){
          this.ampm = 'PM'
        }
        else {
          this.ampm = 'AM'
        }
        if (this.hour < 12){
          this.hour = '0'+ this.hour
        }
        if (minutes < 10){
          this.minutes = '0'+ minutes
        }
        else{
          this.minutes = minutes
        }
        if (seconds < 10){
          this.seconds = '0'+ seconds
        }
        else {
          this.seconds = seconds
        }
      }
    },
    created(){
      this.getTime()
      setInterval(this.getTime,1000)
      this.$store.dispatch('changenow',this.weekday[new Date().getDay()])
    },
}
</script>

<style>

</style>