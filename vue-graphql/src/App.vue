<template>
  <div id="app">
    <img id="logo" alt="Vue logo" src="./assets/harry_potter.jpeg">
    <add-movie/>
    <movies-list/>
  </div>
</template>

<script>
import MoviesList from "./components/MoviesList.vue";
import AddMovie from "./components/AddMovie.vue";

export default {
  name: "app",
  components: {
    MoviesList,
    AddMovie
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#logo {
  width: 400px;
  margin-bottom: 50px;
}
</style>
