/* ============
 * Actions for the country module
 * ============
 *
 * The actions that are available on the
 * country module.
 */

import CountryProxy from '@/proxies/CountryProxy'
import Transformer from '@/transformers/CountryTransformer';
import * as types from './mutation-types';

export const find = ({ commit }) => {
};

export const index = ({ commit }) => {
  new CountryProxy()
    .index()
    .then((response) => {
      commit(types.INDEX, response);
    })
    .catch(() => {
      console.log('Request failed...');
    });
};

export default {
  find,
  index
};
