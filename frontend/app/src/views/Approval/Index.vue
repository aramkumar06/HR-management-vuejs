<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="info">
      <span slot="header">
        Delegate Month Earnings
      </span>

      <div slot="body">
        <div class="row mb-5">
          <div class="col-4">
            <select
              class="form-control"
              v-model="filterObject.account_id"
              >
              <option label=""></option>
              <option
                v-for="paymentAccount in paymentAccounts"
                :value="paymentAccount.id">
                {{ paymentAccount.site_name + ' <' + paymentAccount.account_first_name + ' ' + paymentAccount.account_last_name + '>' }}
              </option>
            </select>
          </div><!-- end of payment-->
          <div class="col-3">
            <select
              class="form-control"
              v-model="filterObject.user_id"
              >
              <option label=""></option>
              <option v-for="user in users" :value="user.id">
                {{ user.name }}
              </option>
            </select>
          </div><!-- end of member-->
          <div class="col-2">
            <select
              class="form-control"
              v-if="years && years.length > 0"
              v-model="filterObject.year"
              v-on:change="populateMonths()"
            >
              <option
                v-for="year in years"
                :value="year.value"
              >
                {{ year.caption }}
              </option>
            </select>
          </div>
          <div class="col-2">
            <select
              class="form-control"
              v-if="months && months.length > 0"
              v-model="filterObject.month"
            >
              <option
                v-for="month in months"
                :value="month.value"
              >
                {{ month.caption }}
              </option>
            </select>
          </div>
          <div class="col-1">
            <button
              class="btn btn-xs btn-primary pull-right"
              @click="getDelegationMonthEarnings()"
            >
              Filter
            </button>
          </div>
        </div><!-- end of filter -->

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
                Comments
              </th>
              <th></th>
              <th></th>
            </thead>
            <tbody v-if="earnings.length > 0">
              <tr
                v-for="earning in earnings"
              >
                <td>
                  {{ earning.member_last_name + ' ' + earning.member_first_name }}
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
                  {{ earning.comments }}
                </td>
                <td>
                  <a
                    class="btn btn-sm btn-success"
                    v-if="earning.approved == false"
                    @click="approvePendingEarning(earning)"
                  >
                    Approve
                  </a>
                  <strong
                    class="text-success"
                    v-if="earning.approved == true"
                  >
                    Approved
                  </strong>
                </td>
                <td>
                  <router-link
                    :to="{name: 'approval.update', params: {earning_id: earning.id}}"
                    class="btn btn-sm btn-warning"
                    v-if="earning.approved == false"
                  >
                    Edit
                  </router-link>
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
  import AccountProxy from '@/proxies/AccountProxy.js';
  import UserProxy from '@/proxies/UserProxy.js';
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
        earnings: [],
        years: [],
        months: [],
        filterObject: {
          year: null,
          month: null,
          account_id: null,
          user_id: null,
        },
        paymentAccounts: [],
        users: [],
      };
    },
    computed: {
    },
    mounted() {
      if (typeof(this.$route.query['year']) === 'undefined' || this.$route.query['year'] === null) {
        this.filterObject.year = store.state.auth.app.active_year;
      } else {
        this.filterObject.year = this.$route.query['year']
      }

      if (typeof(this.$route.query['month']) === 'undefined' || this.$route.query['month'] === null) {
        this.filterObject.month = store.state.auth.app.active_month;
      } else {
        this.filterObject.month = this.$route.query['month'];
      }

      this.populateYears();
      this.populateMonths();

      this.getDelegationMonthEarnings();

      this.getPaymentAccounts();
      this.getDelegationMembers();
    },
    methods: {
      dollarFormat(value) {
        return NumberUtil.currencyFormatter(value);
      },
      populateYears() {
        for (const key of Object.keys(this.$store.state.auth.app.book_dates)) {
          this.years.push({ value: key, caption: key});
        }
      },
      populateMonths() {
        if (typeof(this.filterObject.year) === 'undefined' || this.filterObject.year === null || this.months.length > 0) {
          return;
        }

        for (const key of this.$store.state.auth.app.book_dates[this.filterObject.year]) {
          this.months.push({ value: key, caption: key })
        }
      },
      getDelegationMonthEarnings() {
        this.isLoading = true;
        new EarningProxy().getDelegationMonthEarnings(this.filterObject)
          .then((response) => {
            if (response.success == true) {
              this.earnings = response.earnings;
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
          });
      },
      approvePendingEarning(earning) {
        if (earning == "undefined" || earning == null) {
          console.log('earning is undefined or null');
        }
        if (earning.id == "undefined" || earning.id == null) {
          console.log('id is undefined or null');
        }

        new EarningProxy().approvePendingEarning(earning.id)
          .then((response) => {
            if (response.success === true) {
              earning.approved = true;
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
          });

        return false;
      },
      getPaymentAccounts: function() {
        this.isLoading = true;
        new AccountProxy().payments()
          .then((response) => {
            if (response.success == true) {
              this.paymentAccounts = response.accounts;
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
          .catch((error) => {
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
          });
      },
      getDelegationMembers() {
        this.isLoading = true;
        new UserProxy().index()
          .then((response) => {
            if (response.success == true) {
              this.users = response.users;
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
          .catch((error) => {
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
          });
      },
    },
  };
</script>
