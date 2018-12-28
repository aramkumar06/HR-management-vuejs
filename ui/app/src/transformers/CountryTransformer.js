/* ============
 * Country Transformer
 * ============
 *
 * The transformer for the country.
 */

import Transformer from './Transformer';

export default class CountryTransformer extends Transformer {
  /**
   * Method used to transform a fetched country.
   *
   * @param country The fetched country.
   *
   * @returns {Object} The transformed country.
   */
  static fetch(country) {
    return {
    };
  }

  /**
   * Method used to transform a send country.
   *
   * @param country The country to be send.
   *
   * @returns {Object} The transformed country.
   */
  static send(country) {
    return {
    };
  }
}
