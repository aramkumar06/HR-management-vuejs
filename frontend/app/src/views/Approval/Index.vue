<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Delegate Pending Earnings
      </span>

      <div slot="body">
        <div
          class="row"
          v-if="!isLoading"
          >
          <table class="table">
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
                  {{ dollarFormat(earning.cost) }}
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
        <div class="loading-parent">
          <loading
            :active.sync="isLoading"
            :can-cancel=false
            :is-full-page=true />
        </div>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
/* ============
 * Approval Index Page
 * ============
 *
 * The approval index page.
 */

  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
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
      Loading,
      VLayout,
      VCard,
    },
    data() {
      return {
        isLoading: false,
        pendingEarnings: [],
      };
    },
    computed: {
    },
    mounted() {
      this.getPendingEarnings();
    },
    methods: {
      dollarFormat(value) {
        return NumberUtil.currencyFormatter(value);
      },
      getPendingEarnings() {
        this.isLoading = true;
//        const params = { team_id: this.$store.state.auth.user.team_id };
        const params = {}
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
        new EarningProxy().approvePendingEarning(earning_id)
          .then((response) => {
            if (response.success === true) {
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
