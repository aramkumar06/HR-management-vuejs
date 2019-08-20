import BaseProxy from './Proxy';

class ReportProxy extends BaseProxy {
  /**
   * The constructor for the EarningProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('api/v1/tms/reports', parameters);
  }

  /**
   * Method used to fetch earnings by team members from the API.
   *
   * @returns {Promise} The result in a promise
   */
  members(parameters={}) {
    const member_url = this.endpoint + '/member/';
    return this.submit('post', `/${member_url}`, parameters)
  }

  /**
   * Method used to fetch earnings by teams from the API.
   *
   * @returns {Promise} The result in a promise
   */
  teams(parameters={}) {
    const team_url = this.endpoint + '/team/';
    return this.submit('post', `/${team_url}`, parameters)
  }

  /**
   * Method used to fetch earnings by delegate from the API.
   *
   * @returns {Promise} The result in a promise
   */
  delegate(parameters={}) {
    const delegate_url = this.endpoint + '/delegate/';
    return this.submit('post', `/${delegate_url}`, parameters)
  }

  /**
   * Method used to fetch year total earnings per delegate member from the API.
   *
   * @returns {Promise} The result in a promise
   */
  totalPerDelegateMember(parameters={}) {
    const total_earning_url = this.endpoint + '/total_monthly_per_member/';
    return this.submit('post', `/${total_earning_url}`, parameters)
  }

  /**
   * Method used to fetch year total earnings for all delegate members from the API.
   *
   * @returns {Promise} The result in a promise
   */
  totalByDelegateMembers(parameters={}) {
    const url = this.endpoint + '/total_summary_by_member/';
    return this.submit('post', `/${url}`, parameters)
  }
}

export default ReportProxy;
