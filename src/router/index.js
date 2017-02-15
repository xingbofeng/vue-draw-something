import Vue from 'vue'
import Router from 'vue-router'
import Canvas from 'components/Canvas'
import Guess from 'components/Guess'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/paint',
      name: 'Canvas',
      component: Canvas
    },
    {
      path: '/guess',
      name: 'Guess',
      component: Guess
    }
  ]
})
