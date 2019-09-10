<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="info">
      <span slot="header">
        Reward
      </span>

      <div slot="body">
        <div v-if="!isLoading">
          <div class="row mb-5">
            <table class="table">
              <thead>
                <th></th>
                <th>
                  Team Name
                </th>
                <th>
                  Last rewarded date
                </th>
                <th>
                  From last rewarded
                </th>
                <th>
                  After last rewarded
                </th>
                <th></th>
              </thead>

              <tbody>
                <tr v-for="(reward, index) in teamRewards">
                  <td>{{ index + 1 }}</td>
                  <td>{{ reward.team_name }}</td>
                  <td>{{ reward.rewarded_date }}</td>
                  <td>{{ dollarFormat(reward.initial_amount) }}</td>
                  <td>{{ dollarFormat(reward.cost) }}</td>
                  <td>
                    <button
                      class="btn btn-primary"
                      :disabled="!reward.can_reward"
                      @click="awardNew(reward.team_id)"
                    >Reward</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="loading-parent">
          <loading
            :active.sync="isLoading"
            :can-cancel=false
            :is-full-page=true />
        </div>
      </div>

      <span slot="footer"></span>
    </v-card>
  </v-layout>
</template>

<script>
  /* ============
  * Reward Index Page
  * ============
  *
  * The reward index page
  */

  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import store from '@/store';
  import RewardProxy from '@/proxies/RewardProxy.js';
  import NumberUtil from '@/utils/NumberUtil.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'RewardIndex',

    /**
     * The components that the page can use.
     */
    components: {
      Loading,
      VLayout,
      VCard,
    },
    data() {
      return {
        isLoading: false,
        teamRewards: [],
      };
    },
    mounted() {
      this.getTeamsRewards();
    },
    computed: {},
    methods: {
      dollarFormat(value) {
        return NumberUtil.currencyFormatter(value);
      },
      awardNew(team_id) {
        const params = { team_id: team_id };
        this.isLoading = true;
        new RewardProxy().awardBonus(params)
          .then((response) => {
            if (response.success == true) {
              this.getTeamsRewards();
              this.$notify({
                group: 'notify',
                type: 'success',
                title: 'Success',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            } else {
              this.$notify({
                group: 'notify',
                type: 'error',
                title: 'Error occurred',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            }
          })
          .catch(() => {
            this.$notify({
              group: 'notify',
              type: 'error',
              title: 'Error occurred',
              text: 'Something went wrong',
              duration: 3000,
              speed: 1000,
            });
          })
          .finally(() => {
            this.isLoading = false;
          })
      },
      getTeamsRewards() {
        this.isLoading = false;
        new RewardProxy().getTeamsRewards()
          .then((response) => {
            if (response.success == true) {
              this.teamRewards = response.data;
              this.$notify({
                group: 'notify',
                type: 'success',
                title: 'Success',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            } else {
              this.$notify({
                group: 'notify',
                type: 'error',
                title: 'Error occurred',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            }
          })
          .catch(() => {
            this.$notify({
              group: 'notify',
              type: 'error',
              title: 'Error occurred',
              text: 'Something went wrong',
              duration: 3000,
              speed: 1000,
            });
          })
          .finally(() => {
            this.isLoading = false;
          })
      },
    },
  };
</script>
