/* ============
 * Actions for the project module
 * ============
 *
 * The actions that are available on the
 * project module.
 */

import Vue from 'vue';
import store from '@/store';
import ProjectProxy from '@/proxies/ProjectProxy';
import Transformer from '@/transformers/ProjectTransformer';
import * as types from './mutation-types';

export const find = ({ commit }, payload) => {
  return new ProjectProxy.find(payload);
};

export const index = ({ commit }) => {
  return new ProjectProxy().index();
};

export const create = ({ commit }, payload) => {
  new ProjectProxy()
    .create(payload)
    .then((response) => {
      if (response.success === true) {
        store.dispatch('project/index');
        Vue.router.push({
          name: 'project.index',
        });
      } else {
        /*
         * TODO
         * should integrate with vuejs notification
         */
        console.log('Request failed...');
      }
    })
    .catch(() => {
      console.log('Request failed...');
    });
};

export const update = ({ commit }, payload) => {
  new ProjectProxy()
    .update(payload.id, payload.data)
    .then((response) => {
      if (response.success === true) {
        store.dispatch('project/index');
        Vue.router.push({
          name: 'project.index',
        });
      } else {
        /*
         * TODO
         * should integrate with vuejs notification
         */
        console.log('Request failed...');
      }
    })
    .catch(() => {
      console.log('Request failed...');
    });
};

export default {
  find,
  index,
  create,
  update,
};
