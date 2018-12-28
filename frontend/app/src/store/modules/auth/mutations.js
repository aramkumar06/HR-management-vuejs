/* ============
 * Mutations for the auth module
 * ============
 *
 * The mutations that are available on the
 * account module.
 */

import Vue from 'vue';
import {
  CHECK,
  REGISTER,
  LOGIN,
  LOGOUT,
} from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [CHECK](state) {
    state.authenticated = !!localStorage.getItem('token');
    if (state.authenticated) {
      state.user = {};
      state.user.id = localStorage.getItem('user_id');
      state.user.role_id = localStorage.getItem('user_role_id');
      state.user.role_name = localStorage.getItem('user_role_name');
      state.user.team_id = localStorage.getItem('user_team_id');
      Vue.$http.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
    }
  },

  [REGISTER]() {
    //
  },

  [LOGIN](state, user) {
    state.authenticated = true;
    state.user = user;
    localStorage.setItem('token', user.token);
    localStorage.setItem('user_id', user.id);
    localStorage.setItem('user_role_id', user.role_id);
    localStorage.setItem('user_role_name', user.role_name);
    localStorage.setItem('user_team_id', user.team_id);
    Vue.$http.defaults.headers.common.Authorization = `Token ${user.token}`;
  },

  [LOGOUT](state) {
    state.authenticated = false;
    state.user = null;
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    Vue.$http.defaults.headers.common.Authorization = '';
  },
};
