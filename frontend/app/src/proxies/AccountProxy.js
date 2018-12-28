import store from '@/store';
import Proxy from './Proxy';

class AccountProxy extends Proxy {
  /**
   * The constructor for the AccountProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/accounts', parameters);
  }

  /**
   * Method used to fetch all accounts from the API.
   *
   * @returns {Promise} The result in a promise.
   */
  index() {
    return this.submit('get', `/${this.endpoint}?user_id=${store.state.auth.user.id}`);
  }
}

export default AccountProxy;
