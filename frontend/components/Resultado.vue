<template>
  <v-card>
    <v-card-title>Resultado</v-card-title>
    <v-card-text>
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th id="key" class="text-left">Nombre</th>
              <th id="value" class="text-left">Valor</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in Object.keys(result)" :key="item">
              <td>{{ item.toUpperCase() }}</td>
              <td>{{ result[item] }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    result: Object,
  },
  data() {
    return {};
  },
};
</script>
