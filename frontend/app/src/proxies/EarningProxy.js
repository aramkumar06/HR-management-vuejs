import BaseProxy from './Proxy';

class EarningProxy extends BaseProxy {
  /**
   * The constructor for the EarningProxy.
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
   */
  index() {
    return this.submit('get', `/${this.endpoint}`);
  }

  /**
   * Method used to fetch all pending earnings from the API.
   *
   * @returns {Promise} The result in a promise
   */
  getPendingEarnings(parameters={}) {
    const pending_earning_url = this.endpoint + '/get_pending_earnings/';
    return this.submit('post', `/${pending_earning_url}`, parameters)
  }

  /**
   * Method used to approve pending earning from the API.
   *
   * @returns {Promise} The result in a promise
   */
  approvePendingEarning(earning_id) {
    const pending_approve_url = this.endpoint + '/' + earning_id + '/approve/';
    return this.submit('post', `/${pending_approve_url}`)
  }

  /**
   * Method used to delete pending earning from the API.
   *
   * @returns {Promise} The result in a promise
   */
  deletePendingEarning(earning_id) {
    const pending_delete_url = this.endpoint + '/' + earning_id + '/delete/';
    return this.submit('post', `/${pending_delete_url}`)
  }
}

export default EarningProxy;
