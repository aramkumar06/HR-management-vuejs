/* ============
 * Site Transformer
 * ============
 *
 * The transformer for the site.
 */

import Transformer from './Transformer';

export default class SiteTransformer extends Transformer {
  /**
   * Method used to transform a fetched site.
   *
   * @param site The fetched site.
   *
   * @returns {Object} The transformed site.
   */
  static fetch(site) {
    return {
    };
  }

  /**
   * Method used to transform a send site.
   *
   * @param site The site to be send.
   *
   * @returns {Object} The transformed site.
   */
  static send(site) {
    return {
    };
  }
}
