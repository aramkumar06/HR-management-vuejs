/* ============
 * Actions for the site module
 * ============
 *
 * The actions that are available on the
 * site module.
 */

import SiteProxy from '@/proxies/SiteProxy'
import Transformer from '@/transformers/SiteTransformer';
import * as types from './mutation-types';

export const find = ({ commit }) => {
};

export const index = ({ commit }) => {
  new SiteProxy()
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
