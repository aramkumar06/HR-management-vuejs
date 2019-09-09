<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        My Earnings
      </span>

      <div slot="body">
        <div v-if="!isLoading">
          <div class="row mb-5">
            <div class="col-7">
              <router-link
                :to="{ name: 'earning.create' }"
                class="btn btn-success"
              >
                Add New Earning
              </router-link>
            </div>
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
                @click="queryEarnings()"
              >
                Filter
              </button>
            </div>
          </div>

          <table class="table">
            <thead>
              <th>
                Site
              </th>
              <th>
                Account
              </th>
              <th>
                Cost
              </th>
              <th>
                Status
              </th>
              <th>
                Actioned Date
              </th>
              <th>
                Approval
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
                  {{ earning.site_name }}
                </td>
                <td>
                  {{ earning.account_first_name }} {{ earning.account_last_name }}
                </td>
                <td>
                  {{ dollarFormat(earning.cost) }}
                </td>
                <td>
                  {{ earning.status }}
                </td>
                <td>
                  {{ earning.withdrawn_date }}
                </td>
                <td>
                  <strong v-if="earning.approved == true">
                    Approved
                  </strong>
                  <strong v-if="earning.approved != true">
                    Not approved
                  </strong>
                </td>
                <td>
                  {{ earning.comments }}
                </td>
                <td>
                  <router-link
                    :to="{name: 'earning.update', params: {earning_id: earning.id}}"
                    class="btn btn-sm btn-warning"
                    v-if="earning.approved != true"
                  >
                    Edit
                  </router-link>
                </td>
                <td>
                  <button
                    class="btn btn-sm btn-danger"
                    v-if="earning.approved != true"
                    @click="removeEarning(earning.id)"
                  >
                    Remove
                  </button>
                </td>
              </tr>
            </tbody>
          </table>

          <br />

          <div class="row">
            <div class="col-9">
            </div>
            <div class="col-1">
              <strong>
                Total :
              </strong>
            </div>
            <div class="col-2">
              <strong v-if="summary != null">
                {{ dollarFormat(summary) }}
              </strong>
            </div>
          </div>
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
    name: 'EarningIndex',

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
        years: [],
        months: [],
        filterObject: {
          year: null,
          month: null,
        },
        earnings: [],
        summary: null,
        isLoading: false,
        options: null,
      }
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

      this.queryEarnings();
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
      queryEarnings() {
        this.isLoading = true;
        new EarningProxy(this.filterObject).index()
          .then((response) => {
            if (response.success === true) {
              this.earnings = response.earnings;
              this.summary = response.summary;
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
      removeEarning(earning_id) {
        this.isLoading = true;
        new EarningProxy().deletePendingEarning(earning_id)
          .then((response) => {
            if (response.success === true) {
              this.queryEarnings();
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
