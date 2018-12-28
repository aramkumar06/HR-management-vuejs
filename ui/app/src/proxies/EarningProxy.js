import Proxy from './Proxy';

class EarningProxy extends Proxy {
  /**
   * The constructor for the ClientProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/earnings', parameters);
  }
}

export default EarningProxy;
