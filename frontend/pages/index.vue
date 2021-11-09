<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-text>
          <v-tabs
            v-model="tab"
            background-color="transparent"
            color="primary"
            grow
          >
            <v-tab v-for="item in items" :key="item">
              {{ item }}
            </v-tab>
          </v-tabs>

          <v-tabs-items v-model="tab">
            <v-tab-item>
              <v-card flat>
                <Derivadas />
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <Integrales />
              </v-card>
            </v-tab-item>
          </v-tabs-items>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Derivadas from '../components/Derivadas.vue'
import Integrales from '../components/Integrales.vue'

  export default {
    components: {
      Derivadas,
      Integrales
    },
    data () {
      return {
        tab: null,
        items: [
          'Derivadas', 'Integrales definidas'
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>
