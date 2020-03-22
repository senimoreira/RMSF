<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Análise das Matriculas</h1>
        <hr><br><br>
        <br><br>
         <button type="button"
                class="btn btn-success btn-sm"
                v-b-modal.matricula-modal> Adicionar Matricula </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Matricula</th>
              <th scope="col">Hora de entrada</th>
              <th scope="col">Hora de saída</th>

              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(matricula, index) in matriculas" :key="index">
              <td>{{matricula.matricula}}</td>
              <td>{{matricula.hora_entrada}}</td>
              <td>{{matricula.hora_saida}}</td>
              <td></td>

              <td>
                <div class="btn-group" role="group">
                  <button type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteMatricula(matricula)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addMatriculaModal"
            id="matricula-modal"
            title="Add a new Matricula"
            hide-footer>
      <b-form @submit="onSubmit" class="w-100">
        <b-form-group id="form-matricula-group"
                      label="matricula:"
                      label-for="form-matricula-input">
            <b-form-input id="form-matricula-input"
                          type="text"
                          v-model="addMatriculaForm.matricula"
                          required
                          placeholder="Introduzir Matricula">
            </b-form-input>
          </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Matriculas',
  data() {
    return {
      matriculas: [],
      addMatriculaForm: {
        matricula: '',
      },
    };
  },
  methods: {
    getMatriculas() {
      const path = 'http://localhost:5000/matriculas';
      axios.get(path)
        .then((res) => {
          this.matriculas = res.data.matriculas;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMatricula(answer) {
      const path = 'http://localhost:5000/postMatricula';
      axios.post(path, answer)
        .then(() => {
          this.getMatriculas();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMatriculas();
        });
    },
    initForm() {
      this.addMatriculaForm.matricula = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMatriculaModal.hide();
      const answer = { matricula: this.addMatriculaForm.matricula };
      this.addMatricula(answer);
      this.initForm();
    },
    removeMatricula(matricula) {
      const path = `http://localhost:5000/matriculas/${matricula}`;
      axios.delete(path)
        .then(() => {
          this.getMatriculas();
          this.message = 'Matricula removed!';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMatriculas();
        });
    },
    onDeleteMatricula(matricula) {
      this.removeMatricula(matricula.matricula);
    },
  },
  created() {
    this.getMatriculas();
  },
};
</script>
