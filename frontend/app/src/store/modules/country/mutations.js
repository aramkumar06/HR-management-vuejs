/* ============
 * Mutations for the country module
 * ============
 *
 * The mutations that are available on the
 * country module.
 */

import { FIND, INDEX } from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [FIND](state, country) {
  },
  [INDEX](state, countries) {
    state.countries = countries;
  }
};
