<template>
  <v-app>

    <v-content>
      <BaseLine/>
    </v-content>
  </v-app>
</template>

<script>
import BaseLine from './components/BaseLine';

export default {
  name: 'App',

  components: {
    BaseLine,
  },

  data: () => ({
    //
  }),
};
</script>
