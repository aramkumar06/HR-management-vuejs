import Proxy from './Proxy';

class CountryProxy extends Proxy {
  /**
   * The constructor for the CountryProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/countries', parameters);
  }

  /**
   * Method used to fetch all countries from the API.
   *
   * @returns {Promise} The result in a promise.
   */
  index() {
    return this.all();
  }
}

export default CountryProxy;
