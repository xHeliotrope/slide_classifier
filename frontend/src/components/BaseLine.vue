<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link @click="setActiveWindow('1')">
          <v-list-item-action>
            <v-icon>mdi-folder-multiple-image</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Slide List</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="setActiveWindow('2')">
          <v-list-item-action>
            <v-icon>mdi-telescope</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Current Slide</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="setActiveWindow('3')">
          <v-list-item-action>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Review Classifications</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Digital Slide Classification Demo</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
					v-show="active_window == 1"
        >
          <v-col class="text-center">
            Window 1
            <v-row
              :align="alignment"
              :justify="justify"
              class="grey lighten-5"
              style="height: 300px;"
            >
              <v-card
                v-for="slide in slides_list"
                :key="slide.id"
                class="ma-3 pa-6"
                outlined
                tile
               >
                 <img v-bind:src="getSrc(slide)" v-bind:alt="slide"/>
                   {{ slide }}
                 </v-card>
            </v-row>
          </v-col>
        </v-row>
        <v-row
          align="center"
          justify="center"
					v-show="active_window == 2"
        >
          <v-col class="text-center">
					Window 2
          </v-col>
        </v-row>
        <v-row
          align="center"
          justify="center"
					v-show="active_window == 3"
        >
          <v-col class="text-center">
					Window 3
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
	import axios from 'axios'

  export default {
		name: 'BaseLine',

    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
			active_window: 1,
			slides_list: [],
    }),
		methods: {
      setActiveWindow: function(window_number) {
        this.active_window = window_number
      },
      getSrc: function(slide){
          return "/thumbnail/" + slide
      }
    },
    mounted () {
      axios
        .get('/list_slides')
        .then(response => (this.slides_list = response.data))
    }
  }
</script>
