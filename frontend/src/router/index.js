import Vue from 'vue';
import Router from 'vue-router';
import Matriculas from '../components/Matriculas.vue';
import Sensor from '../components/Sensor.vue';
import Home from '../components/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/sensor',
      name: 'Sensor',
      component: Sensor,
    },
    {
      path: '/matriculas',
      name: 'Matriculas',
      component: Matriculas,
    },
  ],
});
