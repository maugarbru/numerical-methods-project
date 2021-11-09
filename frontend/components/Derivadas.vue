<template>
  <div>
    <v-card>
      <v-card-title>Derivadas</v-card-title>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="x"
          :rules="rules1"
          label="X (Punto a evaluar)"
          type="number"
          outlined
          required
        ></v-text-field>

        <v-text-field
          v-model="delta"
          :rules="rules1"
          label="Delta"
          type="number"
          outlined
          required
        ></v-text-field>

        <v-text-field
          v-model="f"
          :counter="20"
          :rules="rules2"
          label="Función (con formato de python)"
          type="text"
          outlined
          required
        ></v-text-field>

        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="validate"
        >
          Validar
        </v-btn>

        <v-btn color="error" class="mr-4" @click="reset">Borrar</v-btn>
      </v-form>
    </v-card>
    <v-dialog v-model="openResult" max-width="290">
      <Resultado v-if="resultado" :open="openResult" :result="resultado" />
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import Resultado  from './Resultado.vue'

export default {
  components: {
    Resultado
  },
  data: () => ({
    url: "http://ec2-3-22-171-170.us-east-2.compute.amazonaws.com:8000/api/derivadas/",
    // url: "http://localhost:8000/api/derivadas/",
    valid: true,
    x: 3,
    delta: 0.001,
    f: "x**2",
    rules1: [(v) => !!v || "Campo Requerido"],
    rules2: [
      (v) => !!v || "Campo Requerido",
      (v) => (v && v.length <= 30) || "Menos de 30 caracteres",
    ],
    openResult: false,
    resultado: undefined
  }),

  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.calcularDerivada();
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    calcularDerivada() {
      const self = this;
      axios
        .post(this.url, {
          x: this.x,
          delta: this.delta,
          f: this.f,
        })
        .then(function (response) {
          console.log(response);
          self.resultado = response.data;
          self.openResult = true;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
