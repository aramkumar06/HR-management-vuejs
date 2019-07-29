<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Team Pending Earnings
      </span>

      <div slot="body">
        <table class="table table-striped">
          <thead>
            <th>
              Member
            </th>
            <th>
              Site
            </th>
            <th>
              Account
            </th>
            <th>
              Amount
            </th>
            <th>
              Date
            </th>
            <th>
            </th>
          </thead>
          <tbody v-if="pendingEarnings.length > 0">
            <tr
              v-for="earning in pendingEarnings"
            >
              <td>
                {{ earning.member_first_name + ' ' + earning.member_last_name }}
              </td>
              <td>
                {{ earning.site_name }}
              </td>
              <td>
                {{ earning.account_first_name + ' ' + earning.account_last_name }}
              </td>
              <td>
                {{ earning.cost }}
              </td>
              <td>
                {{ earning.withdrawn_date }}
              </td>
              <td>
                <button
                  class="btn btn-sm btn-primary"
                  @click="approvePendingEarning(earning.id)"
                >
                  Approve
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
import VLayout from '@/layouts/Default.vue';
import VCard from '@/components/Card.vue';
import store from '@/store';
import EarningProxy from '@/proxies/EarningProxy.js';
import NumberUtil from '@/utils/NumberUtil.js';

export default {
  /**
   * The name of the page.
   */
  name: 'ApprovalIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
  },
  data() {
    return {
      isLoading: false,
    };
  },
  computed: {
  },
  mounted() {
    this.getPendingEarnings();
  },
  methods: {
    getPendingEarnings() {
      this.isLoading = true;
      const params = { team_id: this.store.state.auth.user.team_id };
      new EarningProxy().getPendingEarnings(params)
        .then((response) => {
          if (response.success == true) {
            this.pendingEarnings = response.pending_earnings;
          } else {
            console.log(response.message);
          }
        })
        .catch((error) => {
          console.log('Request failed...');
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    approvePendingEarning(earning_id) {
      if (earning_id == "undefined" || earning_id == null) {
        console.log('earning_id is undefined or null');
      }

      this.isLoading = true;
      new EarningProxy.approvePendingEarning(params)
        .then((response) => {
          if (response.success == true) {
            this.pendingEarnings = response.pending_earnings;
          } else {
            console.log(response.message);
          }
        })
        .catch((error) => {
          console.log('Request failed...');
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
};
</script>
