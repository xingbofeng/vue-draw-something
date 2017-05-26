import Vue from 'vue';
import Router from 'vue-router';
import store from '../store';
import Paint from '../pages/Paint';
import Guess from '../pages/Guess';
import Home from '../pages/Home';
import About from '../pages/About';
import Login from '../pages/Login';
import Signup from '../pages/Signup';

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: (to, from, next) => {
        // 对于已登陆过的作跳到主页的操作
        if (store.state.login.status === 'error') {
          return next();
        }
        return next({
          path: '/',
        });
      },
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
    {
      path: '/paint',
      name: 'Paint',
      component: Paint,
    },
    {
      path: '/guess',
      name: 'Guess',
      component: Guess,
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup,
    },
  ],
});

/**
 * router.beforeEach对登录权限的认证操作
 * @param  {[Object]} to
 * @param  {[Object]} from
 * @param  {[Object]} }) next
 * @return {[Function]} next
 */
router.beforeEach((to, from, next) => {
  if (store.state.login.status === 'success') {
    return next();
  }
  if (to.path === '/login' || to.path === '/signup') {
    return next();
  }
  return store.dispatch('login', {
    data: {
      username: '',
      password: '',
    },
    next,
  });
});

export default router;

