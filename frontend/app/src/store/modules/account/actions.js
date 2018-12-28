/* ============
 * Actions for the account module
 * ============
 *
 * The actions that are available on the
 * account module.
 */

import Vue from 'vue';
import store from '@/store';
import AccountProxy from '@/proxies/AccountProxy';
import Transformer from '@/transformers/AccountTransformer';
import * as types from './mutation-types';

export const find = ({ commit }, payload) => {
   new AccountProxy()
    .find(payload)
    .then((response) => {
      if (response.success === true) {
        commit(types.FIND, response.account);
      } else {
        console.log('Request failed...');
      }
    })
    .catch(() => {
      console.log('Request failed...');
    });
};

export const index = ({ commit }) => {
  new AccountProxy()
    .index()
    .then((response) => {
      if (response.success === true) {
        commit(types.INDEX, response.accounts);
      } else {
        console.log('Request failed...');
      }
    })
    .catch(() => {
      console.log('Request failed...');
    });
};

export const create = ({ commit }, payload) => {
  new AccountProxy()
    .create(payload)
    .then((response) => {
      if (response.success === true) {
        store.dispatch('account/index');
        Vue.router.push({
          name: 'account.index',
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
  new AccountProxy()
    .update(payload.id, payload.data)
    .then((response) => {
      if (response.success === true) {
        store.dispatch('account/index');
        Vue.router.push({
          name: 'account.index',
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
