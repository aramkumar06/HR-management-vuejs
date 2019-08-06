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
      state.user.is_boss = localStorage.getItem('user_is_boss') === "true";
      Vue.$http.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
      // set whole app variables
      state.app = {};
      state.app.book_dates = JSON.parse(localStorage.getItem('book_dates'));
      state.app.active_year = localStorage.getItem('active_year');
      state.app.active_month = localStorage.getItem('active_month');
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
    localStorage.setItem('user_is_boss', user.is_boss);
    Vue.$http.defaults.headers.common.Authorization = `Token ${user.token}`;
    // set whole app variables
    state.app = {};
    state.app.book_dates = user.book_dates;
    state.app.active_year = user.active_year;
    state.app.active_month = user.active_month;
    localStorage.setItem('book_dates', JSON.stringify(state.app.book_dates));
    localStorage.setItem('active_year', state.app.active_year);
    localStorage.setItem('active_month', state.app.active_month);
  },

  [LOGOUT](state) {
    state.authenticated = false;
    state.user = null;
    state.app = null;
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    localStorage.removeItem('book_dates');
    Vue.$http.defaults.headers.common.Authorization = '';
  },
};
