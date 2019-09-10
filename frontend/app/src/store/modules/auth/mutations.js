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
      state.user = JSON.parse(localStorage.getItem('user'));
      Vue.$http.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
      // set whole app variables
      state.app = {};
      state.app.active_year = state.user.active_year;
      state.app.active_month = state.user.active_month;
      state.app.book_dates = state.user.book_dates;
    }
  },

  [REGISTER]() {
    //
  },

  [LOGIN](state, user) {
    state.authenticated = true;
    state.user = user;
    localStorage.setItem('token', user.token);
    Vue.$http.defaults.headers.common.Authorization = `Token ${user.token}`;
    // set whole app variables
    state.app = {};
    state.app.book_dates = user.book_dates;
    state.app.active_year = user.active_year;
    state.app.active_month = user.active_month;
    localStorage.setItem('user', JSON.stringify(user));
  },

  [LOGOUT](state) {
    state.authenticated = false;
    state.user = null;
    state.app = null;
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    Vue.$http.defaults.headers.common.Authorization = '';
  },
};
