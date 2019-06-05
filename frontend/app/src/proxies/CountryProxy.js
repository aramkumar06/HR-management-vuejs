import BaseProxy from './Proxy';

class CountryProxy extends BaseProxy {
  /**
   * The constructor for the CountryProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/countries', parameters);
  }
}

export default CountryProxy;
