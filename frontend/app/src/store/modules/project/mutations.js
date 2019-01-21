/* ============
 * Mutations for the project module
 * ============
 *
 * The mutations that are available on the
 * project module.
 */

import { FIND, INDEX } from './mutation-types';

/* eslint-disable no-param-reassign */
export default {
  [FIND](state, project) {
    state.project = project;
  },
  [INDEX](state, projects) {
    state.projects = projects;
  },
};
