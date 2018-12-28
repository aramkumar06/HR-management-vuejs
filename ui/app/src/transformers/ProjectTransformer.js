/* ============
 * Project Transformer
 * ============
 *
 * The transformer for the project.
 */

import Transformer from './Transformer';

export default class ProjectTransformer extends Transformer {
  /**
   * Method used to transform a fetched project.
   *
   * @param project The fetched project.
   *
   * @returns {Object} The transformed project.
   */
  static fetch(project) {
    return {
    };
  }

  /**
   * Method used to transform a send project.
   *
   * @param project The earning to be send.
   *
   * @returns {Object} The transformed project.
   */
  static send(project) {
    return {
    };
  }
}
