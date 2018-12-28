/* ============
 * Actions for the earning module
 * ============
 *
 * The actions that are available on the
 * earning module.
 */

import Transformer from '@/transformers/EarningTransformer';
import * as types from './mutation-types';

export const find = ({ commit }) => {
  /*
   * Normally you would use a proxy to fetch the earning:
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
  const earning = {
  };

  commit(types.FIND, Transformer.fetch(earning));
};

export default {
  find,
};
