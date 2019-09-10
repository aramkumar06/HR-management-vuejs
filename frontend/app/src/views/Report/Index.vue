<template>
  <v-layout>
    <v-card contextual-style="info">
      <span slot="header">
        {{ $t('general.report') }}
      </span>
      <div slot="body">
        <div
          v-if="!isLoading"
        >
          <div class="row">
            <div class="col-6">
              <table class="table table-bordered">
                <thead>
                  <th>
                    Name
                  </th>
                  <th>
                    Earn
                  </th>
                  <th class="text-center">
                    Rank
                  </th>
                </thead>
                <tbody>
                  <tr v-for="earning in earnings_by_delegate">
                    <td>
                      {{ earning.name }}
                    </td>
                    <td>
                      {{ dollarFormat(earning.cost) }}
                    </td>
                    <td class="text-center">
                      {{ earning.rank }}
                    </td>
                  </tr>
                  <tr v-if="summary_delegate != null">
                    <td colspan="2" class="text-right">
                      <strong>
                        Total :
                      </strong>
                    </td>
                    <td>
                      {{ dollarFormat(summary_delegate.total) }}
                    </td>
                  </tr>
                  <tr v-if="summary_delegate != null">
                    <td colspan="2" class="text-right">
                      <strong>
                        Average :
                      </strong>
                    </td>
                    <td>
                      {{ dollarFormat(summary_delegate.average) }}
                    </td>
                  </tr>
                  <tr v-if="summary_delegate != null">
                    <td colspan="2" class="text-right">
                      <strong>
                        Percentage :
                      </strong>
                    </td>
                    <td>
                      {{ summary_delegate.percentage }}%
                    </td>
                  </tr>
                </tbody>
              </table>
            </div><!-- end of delegation table -->
            <div class="col-6">
              <table class="table table-bordered">
                <thead>
                  <th>
                    Team Name
                  </th>
                  <th>
                    Earn
                  </th>
                  <th>
                    Average
                  </th>
                  <th class="text-center">
                    Rank
                  </th>
                </thead>
                <tbody>
                  <tr v-for="earning in earnings_by_team">
                    <td>
                      {{ earning.team_name }}
                    </td>
                    <td>
                      {{ dollarFormat(earning.cost) }}
                    </td>
                    <td>
                      {{ dollarFormat(earning.average) }}
                    </td>
                    <td class="text-center">
                      {{ earning.rank }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div><!-- end of team table -->
          </div><!-- end of table -->
          <div class="row mt-4">
            <div class="col-12">
              <v-line-chart
                v-if="delegateEarningsLoaded"
                :chart-data="delegateChartData"
                :options="delegateOptions"
              ></v-line-chart>
            </div>
          </div><!-- end of active month chart -->
          <div class="row mt-4">
            <div class="col-12">
              <v-line-chart
                v-if="totalYearEarningsLoaded"
                :chart-data="totalYearChartData"
                :options="totalYearOptions"
              >
              </v-line-chart>
            </div>
          </div><!-- end of total year chart -->
        </div>
        <div class="loading-parent">
          <loading
            :active.sync="isLoading"
            :can-cancel=false
            :is-full-page=true />
        </div>
      </div>
      <div slot="footer">
        Made by abc
      </div>
    </v-card>
  </v-layout>
</template>

<script>
  /* ============
   * Report Index Page
   * ============
   *
   * The report index page.
   */

  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import store from '@/store';
  import ReportProxy from '@/proxies/ReportProxy.js';
  import VLineChart from '@/components/LineChart.js';
  import NumberUtil from '@/utils/NumberUtil.js';
  import '@/utils/ColorUtil.js';
  import '@/utils/Constants.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'ReportIndex',

    /**
     * The components that the page can use.
     */
    components: {
      Loading,
      VLayout,
      VCard,
      VLineChart,
    },
    data() {
      return {
        isLoading: false,
        filterObject: {
          year: null,
          month: null,
        },
        earnings_by_delegate: [],
        earnings_by_team: [],
        earnings_by_total_year: [],
        summary_delegate: null,
        summary_team: null,
        summary_total_year: null,
        delegateChartData: null,
        teamChartData: null,
        totalYearChartData: null,
        delegateOptions: null,
        teamOptions: null,
        totalYearOptions: null,
        delegateEarningsLoaded: false,
        teamEarningsLoaded: false,
        totalYearEarningsLoaded: false,
      }
    },
    mounted() {
      if (this.$store.state.auth.user.is_boss == true) {
        this.getReportByDelegate();
        this.getReportByTeam();
        this.getReportByTotalYear();
      } else {
      }
    },
    methods: {
      dollarFormat(value) {
        return NumberUtil.currencyFormatter(value);
      },
      getReportByTeam() {
        this.isLoading = true;
        new ReportProxy().teams(this.filterObject)
          .then((response) => {
            if (response.success === true) {
              this.earnings_by_team = response.earnings_by_team;
              this.summary_team = response.summary;

              if (this.earnings_by_team.length > 0) {
                this.teamEarningsLoaded = true;
                this.fillTeamChartData();
              }
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
      getReportByDelegate() {
        this.isLoading = true;
        new ReportProxy().delegate(this.filterObject)
          .then((response) => {
            if (response.success === true) {
              this.earnings_by_delegate = response.earnings_by_delegate;
              this.summary_delegate = response.summary;

              if (this.earnings_by_delegate.length > 0) {
                this.delegateEarningsLoaded = true;
                this.fillDelegateChartData();
              }
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
      getReportByTotalYear() {
        this.isLoading = true;
        const params = { year: (new Date()).getFullYear() };
        new ReportProxy().totalByDelegateMembers(params)
          .then((response) => {
            if (response.success === true) {
              this.earnings_by_total_year = response.earnings;
              this.summary_total_year = response.summary;

              if (this.earnings_by_total_year.length > 0) {
                this.totalYearEarningsLoaded = true;
                this.fillTotalYearChartData();
              }
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
      fillTeamChartData() {
        let labels = [];
        let data = [];
        let backgroundColors = [];
        let suggestedMax;
        let suggestedMin;
        let max = 0;
        let min = 0;

        for (const earning of this.earnings_by_team) {
          labels.push(earning.team_name);
          data.push(earning.cost);
          if (earning.cost > max) {
            max = earning.cost;
          }

          if (earning.cost < min) {
            min = earning.cost;
          }

          if (earning.cost >= window.constants.top_threshold) {
            backgroundColors.push(window.chartColors.green);
          } else if (earning.cost >= window.constants.intermediate_threshold) {
            backgroundColors.push(window.chartColors.blue);
          } else if (earning.cost >= window.constants.elementary_threshold) {
            backgroundColors.push(window.chartColors.orange);
          } else if (earning.cost >= window.constants.last_threshold) {
            backgroundColors.push(window.chartColors.yellow);
          } else {
            backgroundColors.push(window.chartColors.red);
          }
        }

        suggestedMax = max * window.constants.multiplier;
        suggestedMin = min * window.constants.multiplier;

        console.log(backgroundColors);

        this.teamChartData = {
          labels: labels,
          datasets: [
            {
              backgroundColor: backgroundColors,
              label: 'Teams',
              data: data,
              lineTension: 0,
            },
          ],
        };

        this.teamOptions = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                barPercentage: 0.3,
              }
            ],
            yAxes: [
              {
                ticks:
                  {
                    suggestedMin: suggestedMin,
                    suggestedMax: suggestedMax,
                  },
              },
            ],
          }
        };
      },
      fillDelegateChartData() {
        let labels = [];
        let data = [];
        let backgroundColors = [];
        let suggestedMax;
        let suggestedMin;
        let max = 0;
        let min = 0;

        for (const earning of this.earnings_by_delegate) {
          labels.push(earning.name);
          data.push(earning.cost);
          if (earning.cost > max) {
            max = earning.cost;
          }

          if (earning.cost < min) {
            min = earning.cost;
          }

          if (earning.cost >= window.constants.top_threshold) {
            backgroundColors.push(window.chartColors.green);
          } else if (earning.cost >= window.constants.intermediate_threshold) {
            backgroundColors.push(window.chartColors.blue);
          } else if (earning.cost >= window.constants.elementary_threshold) {
            backgroundColors.push(window.chartColors.orange);
          } else if (earning.cost >= window.constants.last_threshold) {
            backgroundColors.push(window.chartColors.yellow);
          } else {
            backgroundColors.push(window.chartColors.red);
          }
        }

        suggestedMax = max * window.constants.multiplier;
        suggestedMin = min * window.constants.multiplier;

        this.delegateChartData = {
          labels: labels,
          datasets: [
            {
              backgroundColor: backgroundColors,
              label: 'Delegate',
              data: data,
              fill: false,
            },
          ],
        };

        this.delegateOptions = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                gridLines: false,
              }
            ],
            yAxes: [
              {
                ticks:
                  {
                    suggestedMin: suggestedMin,
                    suggestedMax: suggestedMax,
                    padding: 50
                  },
                gridLines: false,
              },
            ],
          }
        };
      },
      fillTotalYearChartData() {
        let labels = [];
        let data = [];
        let backgroundColors = [];
        let suggestedMax;
        let suggestedMin;
        let max = 0;
        let min = 0;

        for (const earning of this.earnings_by_total_year) {
          labels.push(earning.name);
          data.push(earning.cost);
          if (earning.cost > max) {
            max = earning.cost;
          }

          if (earning.cost < min) {
            min = earning.cost;
          }

          if (earning.cost >= window.constants.top_threshold) {
            backgroundColors.push(window.chartColors.green);
          } else if (earning.cost >= window.constants.intermediate_threshold) {
            backgroundColors.push(window.chartColors.blue);
          } else if (earning.cost >= window.constants.elementary_threshold) {
            backgroundColors.push(window.chartColors.orange);
          } else if (earning.cost >= window.constants.last_threshold) {
            backgroundColors.push(window.chartColors.yellow);
          } else {
            backgroundColors.push(window.chartColors.red);
          }
        }

        suggestedMax = max * window.constants.multiplier;
        suggestedMin = min * window.constants.multiplier;

        this.totalYearChartData = {
          labels: labels,
          datasets: [
            {
              backgroundColor: backgroundColors,
              label: 'Total Year',
              data: data,
              fill: false,
            },
          ],
        };

        this.totalYearOptions = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                gridLines: false,
              }
            ],
            yAxes: [
              {
                ticks:
                  {
                    suggestedMin: suggestedMin,
                    suggestedMax: suggestedMax,
                    padding: 50
                  },
                gridLines: false,
              },
            ],
          }
        };
      },
    }
  };
</script>
