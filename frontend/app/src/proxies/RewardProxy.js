import BaseProxy from './Proxy';

class RewardProxy extends BaseProxy {
  /**
   * The constructor for the RewardProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters={}) {
    super('api/v1/tms/rewards', parameters)
  }

  /**
   * Method used to get status of rewards for all teams from the API.
   *
   * @returns {Promise} The result in a promise
   */
  getTeamsRewards() {
    const team_rewards_url = this.endpoint + '/list_teams_reward/';
    return this.submit('post', `/${team_rewards_url}`)
  }

  /**
   * Method used to award bonus to team using the API.
   *
   * @returns {Promise} The result in a promise
   */
  awardBonus(parameters={}) {
    const bonus_url = this.endpoint + '/approve_team_reward/';
    return this.submit('post', `/${bonus_url}`, parameters)
  }

}

export default RewardProxy;
