/* ============
 * Actions for the earning module
 * ============
 *
 * The actions that are available on the
 * earning module.
 */

import Vue from 'vue';
import store from '@/store';
import EarningProxy from '@/proxies/EarningProxy';
import Transformer from '@/transformers/EarningTransformer';
import * as types from './mutation-types';

export const find = ({ commit }, payload) => {
  return new EarningProxy().find(payload);
};

export const index = ({ commit }, payload) => {
  return new EarningProxy(payload).index();
};

export const create = ({ commit }, payload) => {
  new EarningProxy()
    .create(payload)
    .then((response) => {
      if (response.success === true) {
        // store.dispatch('earning/index');
        Vue.router.push({
          name: 'earning.index',
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
  new EarningProxy()
    .create(payload)
    .then((response) => {
      if (response.success === true) {
        // store.dispatch('earning/index');
        Vue.router.push({
          name: 'earning.index',
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
