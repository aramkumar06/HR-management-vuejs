/* ============
 * Actions for the client module
 * ============
 *
 * The actions that are available on the
 * client module.
 */

import Vue from 'vue';
import store from '@/store';
import ClientProxy from '@/proxies/ClientProxy';
import Transformer from '@/transformers/ClientTransformer';
import * as types from './mutation-types';

export const find = ({ commit }, payload) => {
  return new ClientProxy().find(payload);
};

export const index = ({ commit }) => {
  return new ClientProxy().index();
};

export const create = ({ commit }, payload) => {
  new ClientProxy()
    .create(payload)
    .then((response) => {
      if (response.success === true) {
        store.dispatch('client/index');
        Vue.router.push({
          name: 'client.index',
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
  new ClientProxy()
    .update(payload.id, payload.data)
    .then((response) => {
      if (response.success === true) {
        store.dispatch('client/index');
        Vue.router.push({
          name: 'client.index',
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
  update
};
