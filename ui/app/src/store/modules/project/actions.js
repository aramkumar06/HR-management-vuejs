/* ============
 * Actions for the project module
 * ============
 *
 * The actions that are available on the
 * project module.
 */

import Transformer from '@/transformers/ProjectTransformer';
import * as types from './mutation-types';

export const find = ({ commit }) => {
  /*
   * Normally you would use a proxy to fetch the project:
   *
   * new Proxy()
   *  .find()
   *  .then((response) => {
   *    commit(types.FIND, Transformer.fetch(response));
   *  })
   *  .catch(() => {
   *    console.log('Request failed...');
   *  });
   */
  const account = {
  };

  commit(types.FIND, Transformer.fetch(account));
};

export default {
  find,
};
