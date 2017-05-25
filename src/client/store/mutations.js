import * as types from './mutation-types';

const mutations = {
  [types.LOGIN](state, login) {
    state.login = login;
  },

  [types.NET_STATUS](state, netStatus) {
    state.netStatus = netStatus;
  },

  [types.LEFT_DRAWER](state, leftDrawer) {
    state.leftDrawer = leftDrawer;
  },
};

export default mutations;
