<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          Classify Tile
        </v-card-title>
         <v-radio-group v-model="selectedRegion" column>
            <v-radio label="Feature Region 1" value="feature1"></v-radio>
            <v-radio label="Precancerous" value="precancerous"></v-radio>
          </v-radio-group>

        <v-card-text>
				Sending coordinates: {{ coords.x }}, {{ coords.y }}, {{ coords.width }}, {{ coords.height }} to save tile to disk and database. 
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="sendCoordinates()"
          >
            Okay
          </v-btn>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
		props: {
      dialog: Boolean,
      coords: Array,
      filename: String,
      regions: Array,
    },
    data () {
      return {
        selectedRegion: '',
      }
    },
    methods: {
      sendCoordinates: function(){
        var that = this
        axios
				.get('slide/save/' + that.filename + '/' + that.selectedRegion + '/' + + that.coords.x + '/' + that.coords.y + '/' + that.coords.width + '/' + that.coords.height)
				.then(function(response) {
          that.dialog = false
				}
			  )
      }
    }
  }
</script>
