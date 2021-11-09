<template>
  <v-app>
    <v-app-bar
      fixed
      app
    >
      <v-spacer />
      <v-toolbar-title>Metodos Númericos</v-toolbar-title>
      <v-spacer />
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      absolute
      app
    >
    <v-spacer />
      <span>Metodos Númericos. UdeM. Mauricio Garzon & Julian Tamayo &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {}
  }
}
</script>
