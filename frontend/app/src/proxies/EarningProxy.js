import BaseProxy from './Proxy';

class EarningProxy extends BaseProxy {
  /**
   * The constructor for the ClientProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/earnings', parameters);
  }
  /**
   * Method used to fetch all earnings from the API.
   *
   * @returns {Promise} The result in a promise.
   *
   * TODO
   * user can query with project_id
   */
  index() {
    return this.submit('get', `/${this.endpoint}`);
  }
}

export default EarningProxy;
