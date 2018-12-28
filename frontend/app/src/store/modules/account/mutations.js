/* ============
 * Mutations for the account module
 * ============
 *
 * The mutations that are available on the
 * account module.
 */

import { FIND, INDEX } from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [FIND](state, account) {
    state.account = account;
  },
  [INDEX](state, accounts) {
    state.accounts = accounts;
  },
};
