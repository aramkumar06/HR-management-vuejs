/* ============
 * Mutations for the site module
 * ============
 *
 * The mutations that are available on the
 * site module.
 */

import { FIND, INDEX } from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [FIND](state, site) {
  },
  [INDEX](state, sites) {
    state.sites = sites;
  }
};
