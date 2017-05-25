import Vue from 'vue';
import Router from 'vue-router';
import Paint from 'pages/Paint';
import Guess from 'pages/Guess';
import Home from 'pages/Home';
import About from 'pages/About';

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/paint',
      name: 'Paint',
      component: Paint
    },
    {
      path: '/guess',
      name: 'Guess',
      component: Guess
    },
  ],
});
