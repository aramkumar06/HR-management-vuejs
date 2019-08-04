import BaseProxy from './Proxy';

class UserProxy extends BaseProxy {
  /**
   * The constructor for the UserProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/users', parameters);
  }

  /**
   * Method used to fetch all members from the API.
   *
   * @returns {Promise} The result in a promise.
   */
  index() {
    return this.all();
  }
}

export default UserProxy;
