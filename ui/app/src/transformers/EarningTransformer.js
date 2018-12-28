/* ============
 * Earning Transformer
 * ============
 *
 * The transformer for the earning.
 */

import Transformer from './Transformer';

export default class EarningTransformer extends Transformer {
  /**
   * Method used to transform a fetched earning.
   *
   * @param earning The fetched earning.
   *
   * @returns {Object} The transformed earning.
   */
  static fetch(earning) {
    return {
    };
  }

  /**
   * Method used to transform a send earning.
   *
   * @param earning The earning to be send.
   *
   * @returns {Object} The transformed earning.
   */
  static send(earning) {
    return {
    };
  }
}
