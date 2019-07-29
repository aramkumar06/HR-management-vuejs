<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <div class="row">
      <div class="col-md-12">
        <router-link
          :to="{ name: 'earning.create' }"
          class="btn btn-success pull-right offset-md-10 col-md-2"
        >
          Add New Earning
        </router-link>
      </div>
    </div>

    <br />

    <v-card contextual-style="dark">
      <span slot="header">
        My Earnings
      </span>

      <div slot="body">
        <div class="row">
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
          <div class="col-3">
            <button
              class="btn btn-xs btn-primary pull-right"
              @click="queryEarnings()"
            >
              Filter
            </button>
          </div>
        </div>

        <br />

        <table class="table table-striped">
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
          </thead>
          <tbody v-if="earnings.length > 0">
            <tr
              v-for="earning in earnings"
            >
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
                {{ earning.status }}
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
  name: 'EarningIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
  },
  data() {
    return {
      years: [],
      months: [],
      weeks: [],
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
      for (const key of Object.keys(store.state.auth.app.book_dates)) {
        this.years.push({ value: key, caption: key});
      }
    },
    populateMonths() {
      if (typeof(this.filterObject.year) === 'undefined' || this.filterObject.year === null || this.months.length > 0) {
        return;
      }

      for (const key of Object.keys(store.state.auth.app.book_dates[this.filterObject.year])) {
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
  },
};
</script>
