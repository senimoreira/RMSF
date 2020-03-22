<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Análise dos sensores</h1>
        <hr><br><br>
        <button type="button"
                class="btn btn-success btn-sm"
                v-b-modal.sensor-modal> Adicionar Sensor </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID do Sensor</th>
              <th scope="col">Estado</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sensor, index) in sensors" :key="index">
              <td>{{sensor.id}}</td>
              <td>{{sensor.estado}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteSensor(sensor)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
      <b-modal ref="addSensorModal"
            id="sensor-modal"
            title="Add a new Sensor"
            hide-footer>
      <b-form @submit="onSubmit" class="w-100">
        <b-form-group id="form-estado-group"
                      label="estado:"
                      label-for="form-estado-input">
            <b-form-input id="form-estado-input"
                          type="text"
                          v-model="addSensorForm.estado"
                          required
                          placeholder="Introduzir estado">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-is-group"
                      label="id:"
                      label-for="form-id-input">
            <b-form-input id="form-id-input"
                          type="text"
                          v-model="addSensorForm.id"
                          required
                          placeholder="Introduzir id">
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
  name: 'Sensor',
  data() {
    return {
      sensors: [],
      addSensorForm: {
        estado: '',
        id: -1,
      },
      message: '',
      editForm: {
        estado: '',
        id: -1,
      },
    };
  },
  methods: {
    getSensors() {
      const path = 'http://localhost:5000/sensors';
      axios.get(path)
        .then((res) => {
          this.sensors = res.data.sensors;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addSensor(answer) {
      const path = 'http://localhost:5000/postSensor';
      axios.post(path, answer)
        .then(() => {
          this.getSensors();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSensor();
        });
    },
    initForm() {
      this.addSensorForm.estado = '';
      this.addSensorForm.id = -1;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSensorModal.hide();
      const answer = {
        estado: this.addSensorForm.estado,
        id: this.addSensorForm.id,
      };
      this.addSensor(answer);
      this.initForm();
    },
    removeSensor(sensorID) {
      const path = `http://localhost:5000/sensors/${sensorID}`;
      axios.delete(path)
        .then(() => {
          this.getSensors();
          this.message = 'Sensor removed!';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSensors();
        });
    },
    onDeleteSensor(sensor) {
      this.removeSensor(sensor.id);
    },
  },
  created() {
    this.getSensors();
  },

};
</script>
