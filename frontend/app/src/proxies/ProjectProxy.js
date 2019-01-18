import Proxy from './Proxy';

class ProjectProxy extends Proxy {
  /**
   * The constructor for the ClientProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/projects', parameters);
  }

  /**
   * Method used to fetch all projects from the API.
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

export default ProjectProxy;
