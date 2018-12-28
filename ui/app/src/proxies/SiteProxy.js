import Proxy from './Proxy';

class SiteProxy extends Proxy {
  /**
   * The constructor for the SiteProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/sites', parameters);
  }

  /**
   * Method used to fetch all sites from the API.
   *
   * @returns {Promise} The result in a promise.
   */
  index() {
    return this.all();
  }
}

export default SiteProxy;
