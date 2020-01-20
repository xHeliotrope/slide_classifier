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
					v-show="activeWindow == 1"
        >
          <v-col class="text-center">
            <v-row
              :align="alignment"
              :justify="justify"
              class="grey lighten-5"
              style="height: 300px;"
            >
              <v-card
                v-for="slide in slidesList"
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
					v-show="activeWindow == 2"
					class="slideRow"
        >
          <v-col class="text-center slideCol">
						<div id="seadragonView"></div>
          </v-col>
        </v-row>
        <v-row
          align="center"
          justify="center"
					v-show="activeWindow == 3"
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
      <span class="white--text">&copy; 2020</span>
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
			labels: ["Feature 1", "Feature 2"],
      drawer: null,
			activeWindow: 1,
			slidesList: [],
			activeSlide: null,
			viewer: null,
			tileSources: '/slide/xml/',
			imageOptions: null,
    }),
		methods: {
      setActiveWindow: function(windowNumber) {
				if (windowNumber == 2) {
					this.initSeadragon()
				}
        this.activeWindow = windowNumber
      },
      getSrc: function(slide) {
          return "/thumbnail/" + slide
      },
			setTileSources: function(slide) {
				this.tileSources = "/tiles/" + slide
			},
      initSeadragon: function() {
				var that = this
        if(!this.viewer) {
					var tileSources = [];
					this.slidesList.forEach(function(slide){
						tileSources.push(that.tileSources + slide);
					});
          this.viewer = new OpenSeadragon(this.getOptions(tileSources));
        }
      },
      getOptions: function(tileSources) {
        return {
          id: "seadragonView",
          tileSources: tileSources,
					sequenceMode: true,
          prefixUrl: "/media/",
          showNavigator: true,
          showRotationControl: true,
          animationTime: 0.5,
          blendTime: 0.1,
          constrainDuringPan: true,
          maxZoomPixelRatio: 2,
          minZoomLevel: 1,
          visibilityRatio: 1,
          zoomPerScroll: 2,
          timeout: 120000
        }
			}
    },
    mounted () {
      this.activeSlide = 'C3L-00452-41.svs';
      axios
        .get('/list_slides')
        .then(response => (this.slidesList = response.data))

    }
  }
</script>
<style scoped>
div#seadragonView {
	height: 100%;
	width: 100%;
}
.slideRow {
	height: 100%;
}

.slideCol {
	height: 100%;
}
</style>
