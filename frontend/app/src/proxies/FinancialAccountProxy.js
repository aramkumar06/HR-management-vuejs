import BaseProxy from './Proxy';

class FinancialAccountProxy extends BaseProxy {
  /**
   * The constructor for the FinancialAccountProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters={}) {
    super('api/v1/tms/financial_accounts', parameters)
  }
}

export default FinancialAccountProxy;
