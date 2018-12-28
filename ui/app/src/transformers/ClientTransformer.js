/* ============
 * Client Transformer
 * ============
 *
 * The transformer for the client.
 */

import Transformer from './Transformer';

export default class ClientTransformer extends Transformer {
  /**
   * Method used to transform a fetched client.
   *
   * @param client The fetched client.
   *
   * @returns {Object} The transformed client.
   */
  static fetch(client) {
    return {
    };
  }

  /**
   * Method used to transform a send client.
   *
   * @param client The client to be send.
   *
   * @returns {Object} The transformed client.
   */
  static send(client) {
    return {
    };
  }
}
