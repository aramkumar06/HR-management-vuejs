/* ============
 * Actions for the client module
 * ============
 *
 * The actions that are available on the
 * client module.
 */

import Transformer from '@/transformers/ClientTransformer';
import * as types from './mutation-types';

export const find = ({ commit }) => {
  /*
   * Normally you would use a proxy to fetch the client:
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
  const client = {
  };

  commit(types.FIND, Transformer.fetch(client));
};

export default {
  find,
};
