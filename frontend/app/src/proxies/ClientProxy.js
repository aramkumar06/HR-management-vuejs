import BaseProxy from './Proxy';

class ClientProxy extends BaseProxy {
  /**
   * The constructor for the ClientProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/clients', parameters);
  }

  /**
   * Method used to fetch all clients from the API.
   *
   * @returns {Promise} The result in a promise.
   *
   * TODO
   * user can query with account_id
   */
  index() {
    return this.submit('get', `/${this.endpoint}`);
  }
}

export default ClientProxy;
