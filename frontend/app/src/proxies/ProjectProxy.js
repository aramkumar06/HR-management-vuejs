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
}

export default ProjectProxy;
