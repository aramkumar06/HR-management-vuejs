<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Delegate Month Earnings
      </span>

      <div slot="body">
        <div class="row mb-5">
          <div class="col-5"></div>
          <div class="col-3">
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
          <div class="col-3">
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
                  <button
                    class="btn btn-sm btn-success"
                    v-if="earning.approved == false"
                    @click="approvePendingEarning(earning)"
                  >
                    Approve
                  </button>
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
        },
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
      approvePendingEarning(earning) {
        if (earning == "undefined" || earning == null) {
          console.log('earning is undefined or null');
        }
        if (earning.id == "undefined" || earning.id == null) {
          console.log('id is undefined or null');
        }

        this.isLoading = true;
        new EarningProxy().approvePendingEarning(earning.id)
          .then((response) => {
            if (response.success === true) {
              earning.approved = true;
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

        return false;
      },
    },
  };
</script>
