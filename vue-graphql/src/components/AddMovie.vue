<template>
  <form @submit="submit">
    <fieldset>
      <input type="text" placeholder="Id" v-model="id">
      <input type="text" placeholder="Title" v-model="title">
      <input type="text" placeholder="Director" v-model="director">
      <input type="text" placeholder="Composer" v-model="composer">
      <input type="text" placeholder="Release date" v-model="release_date">
    </fieldset>
    <input class="button-primary" type="submit" value="Send">
  </form>
</template>

<script>
import gql from "graphql-tag";
import { InMemoryCache } from "apollo-cache-inmemory";

const ADD_MOVIE = gql`
  mutation AddMovie(
    $id: int!
    $title: String!
    $director: String!
    $composer: String!
    $release_date: String!) {
    addMovie(
    id: $id
    title: $title
    director: $director
    composer: $composer
    release_date: $release_date
    ) {
      id
    }
  }
`;

export default {
  name: "AddMovie",
  data() {
    return {
      id: "",
      title: "",
      director: "",
      composer: "",
      release_date: ""
    };
  },
  apollo: {},
  methods: {
    submit(e) {
      e.preventDefault();
      const { id, title, director, composer, release_date } = this.$data;
      this.$apollo.mutate({
        mutation: ADD_MOVIE,
        variables: {
          id,
          title,
          director,
          composer, 
          release_date
        }
      });
    }
  }
};
</script>
