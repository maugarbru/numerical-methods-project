<template>
  <div>
    <v-card>
      <v-card-title>Integrales</v-card-title>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="a"
          :rules="rules1"
          label="A (Limite Inferior)"
          type="number"
          outlined
          required
        ></v-text-field>

        <v-text-field
          v-model="b"
          :rules="rules1"
          label="B (Limite Superior)"
          type="number"
          outlined
          required
        ></v-text-field>

        <v-text-field
          v-model="n"
          :rules="rules1"
          label="N (# Segmentos)"
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
import Resultado from "./Resultado.vue";

export default {
  components: {
    Resultado,
  },
  data: () => ({
    url: 'http://ec2-3-17-203-247.us-east-2.compute.amazonaws.com:8000/api/integrales/',
    // url: "http://localhost:8000/api/integrales/",
    valid: true,
    a: 5,
    b: 10,
    n: 4,
    f: "x**2",
    rules1: [(v) => !!v || "Campo Requerido"],
    rules2: [
      (v) => !!v || "Campo Requerido",
      (v) => (v && v.length <= 30) || "Menos de 30 caracteres",
    ],
    openResult: false,
    resultado: undefined,
  }),

  methods: {
    validate() {
      if (parseFloat(this.b) <= parseFloat(this.a)) {
        alert("B debe ser mayor que A");
      } else if (this.$refs.form.validate()) {
        this.calcularIntegral();
      }
    },
    reset() {
      this.$refs.form.reset();
    },

    calcularIntegral() {
      const self = this;
      axios
        .post(this.url, {
          a: this.a,
          b: this.b,
          n: this.n,
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
