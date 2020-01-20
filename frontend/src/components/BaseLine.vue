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
			viewer: null,
			tileSources: '/slide/xml/',
			imageOptions: null,
			selections: [],
			currentSelection: null,
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
					this.currentSelection = this.viewer.selection(this.getSelectionOptions);
					this.currentSelection.enable();
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
			},
			getSelectionOptions: function() {
        return {
          element:                 null, // html element to use for overlay
          showSelectionControl:    true, // show button to toggle selection mode
          toggleButton:            null, // dom element to use as toggle button
          showConfirmDenyButtons:  true,
          styleConfirmDenyButtons: true,
          returnPixelCoordinates:  true,
          keyboardShortcut:        'c', // key to toggle selection mode
          rect:                    null, // initial selection as an OpenSeadragon.SelectionRect object
          allowRotation:           true, // turn selection rotation on or off as needed
          startRotated:            false, // alternative method for drawing the selection; useful for rotated crops
          startRotatedHeight:      0.1, // only used if startRotated=true; value is relative to image height
          restrictToImage:         false, // true = do not allow any part of the selection to be outside the image
          onSelection:             function(rect) {
            alert(rect + ' Center point: ' + rect.getCenter() + ' Degree rotation: ' + rect.getDegreeRotation());
          }, // callback
          prefixUrl:               null, // overwrites OpenSeadragon's option
          navImages:               { // overwrites OpenSeadragon's options
            selection: {
                  REST:   'selection_rest.png',
                  GROUP:  'selection_grouphover.png',
                  HOVER:  'selection_hover.png',
                  DOWN:   'selection_pressed.png'
              },
              selectionConfirm: {
                  REST:   'selection_confirm_rest.png',
                  GROUP:  'selection_confirm_grouphover.png',
                  HOVER:  'selection_confirm_hover.png',
                  DOWN:   'selection_confirm_pressed.png'
              },
              selectionCancel: {
                  REST:   'selection_cancel_rest.png',
                  GROUP:  'selection_cancel_grouphover.png',
                  HOVER:  'selection_cancel_hover.png',
                  DOWN:   'selection_cancel_pressed.png'
              },
          },
          borderStyle: { // overwriteable style defaults
              width:      '1px',
              color:      '#fff'
          },
          handleStyle: {
              top:        '50%',
              left:       '50%',
              width:      '6px',
              height:     '6px',
              margin:     '-4px 0 0 -4px',
              background: '#000',
              border:     '1px solid #ccc'
          },
           cornersStyle: {
              width:      '6px',
              height:     '6px',
              background: '#000',
              border:     '1px solid #ccc'
          }
        }
      }
    },
    mounted () {
			var that = this
      axios
        .get('/list_slides')
        .then(function(response) {
					that.slidesList = response.data;
				})

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
