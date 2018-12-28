import Proxy from './Proxy';

class ClientProxy extends Proxy {
  /**
   * The constructor for the ClientProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/clients', parameters);
  }
}

export default ClientProxy;
