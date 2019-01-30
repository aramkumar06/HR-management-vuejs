/* ============
 * Mutations for the earning module
 * ============
 *
 * The mutations that are available on the
 * earning module.
 */

import { FIND, INDEX } from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [FIND](state, earning) {
    state.earning = earning;
  },
  [INDEX](state, earnings) {
    state.earnings = earnings;
  }
};
