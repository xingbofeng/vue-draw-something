import router from '../router';
import { LOGIN } from './mutation-types';
import config from '../serverConfig';
import axios from 'axios';

const login = ({ commit, state }, { data, next }) => {
  axios({
    method: 'post',
    url: `${config.server}/api/login`,
    data,
  })
    .then((response) => {
      const status = response.data.status;
      if (status === 'success') {
        // 如果成功登录，则正常跳转
        commit(LOGIN, response.data);
        return next();
      }
      // 否则跳到登录页
      return next({
        path: '/login',
      });
    })
    .catch((error) => {
      // 网络错误则跳到错误页
      return next({
        path: '/error',
      });
    });
}

const actions = {
  login,
};

export default actions;
