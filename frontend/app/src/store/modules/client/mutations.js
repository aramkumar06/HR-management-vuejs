/* ============
 * Mutations for the client module
 * ============
 *
 * The mutations that are available on the
 * client module.
 */

import { FIND, INDEX } from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [FIND](state, client) {
    state.client = client;
  },
  [INDEX](state, clients) {
    state.clients = clients;
  },
};
