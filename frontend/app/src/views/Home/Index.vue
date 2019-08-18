<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        {{ $t('general.welcome') }}
      </span>
      <div slot="body">
        <div
          class="row"
          v-if="!isLoading"
        >
          <div class="col-6">
            <v-bar-chart
              v-if="memberEarningsLoaded"
              :chart-data="memberChartData"
              :options="memberOptions"
            ></v-bar-chart>
          </div>
          <div class="col-6">
            <v-bar-chart
              v-if="teamEarningsLoaded"
              :chart-data="teamChartData"
              :options="teamOptions"
            ></v-bar-chart>
          </div>
          <div class="col-12">
            <v-line-chart
              v-if="yearEarningsLoaded"
              :chart-data="yearChartData"
              :options="yearOptions"
              ></v-line-chart>
          </div>
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
 * Home Index Page
 * ============
 *
 * The home index page.
 */

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import VLayout from '@/layouts/Default.vue';
import VCard from '@/components/Card.vue';
import store from '@/store';
import ReportProxy from '@/proxies/ReportProxy.js';
import VBarChart from '@/components/BarChart.js';
import VLineChart from '@/components/LineChart.js';
import NumberUtil from '@/utils/NumberUtil.js';
import '@/utils/ColorUtil.js';
import '@/utils/Constants.js';

export default {
  /**
   * The name of the page.
   */
  name: 'HomeIndex',

  /**
   * The components that the page can use.
   */
  components: {
    Loading,
    VLayout,
    VCard,
    VBarChart,
    VLineChart,
  },
  data() {
    return {
      isLoading: false,
      filterObject: {
        year: null,
        month: null,
      },
      earnings_by_member: [],
      earnings_by_team: [],
      earnings_by_year: [],
      summary_member: null,
      summary_team: null,
      summary_year: null,
      memberChartData: null,
      teamChartData: null,
      yearChartData: null,
      memberOptions: null,
      teamOptions: null,
      yearOptions: null,
      memberEarningsLoaded: false,
      teamEarningsLoaded: false,
      yearEarningsLoaded: false,
    }
  },
  mounted() {
    this.getReportByMember();
    this.getReportByTeam();
    this.getReportByYear();
  },
  methods: {
    getReportByMember() {
      if (this.$store.state.auth.user.team_id === "undefined" || this.$store.state.auth.user.team_id === null) {
        return;
      }

      this.isLoading = true;
      const params = {
        team_id: this.$store.state.auth.user.team_id,
        year: this.filterObject.year,
        month: this.filterObject.month,
      };

      new ReportProxy().members(params)
        .then((response) => {
          if (response.success === true) {
            this.earnings_by_member = response.earnings_by_member;
            this.summary_member = response.summary;

            if (this.earnings_by_member.length > 0) {
              this.memberEarningsLoaded = true;
              this.fillMemberChartData();
            }
          } else {
            console.log('Error occurred');
          }
        })
        .catch((error) => {
          console.log('Request failed...');
        })
        .finally(() => {
          this.isLoading = false;
        });
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
            console.log('Error occurred');
          }
        })
        .catch((error) => {
          console.log('Request failed...');
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    getReportByYear() {
      const params = { year: (new Date()).getFullYear() };
      this.isLoading = true;
      new ReportProxy().totalByDelegateMembers(params)
        .then((response) => {
          if (response.success == true) {
            this.earnings_by_year = response.earnings;
            this.summary_year = response.summary;
            if (this.earnings_by_year.length > 0) {
              this.yearEarningsLoaded = true;
              this.fillYearChartData();
            } else {
              console.log('Error occurred');
            }
          }
        })
        .catch((error) => {
          console.log('Request failed...');
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    fillMemberChartData() {
      let labels = [];
      let data = [];
      let backgroundColors = [];
      let suggestedMax;
      let suggestedMin;
      let max = 0;
      let min = 0;
      let index = 0;

      for (const earning of this.earnings_by_member) {
        labels.push(earning.name);
        data.push(earning.cost);
        index = index + 1;
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

      this.memberChartData = {
        labels: labels,
        datasets: [
          {
            backgroundColor: backgroundColors,
            label: 'Members',
            data: data,
            lineTension: 0,
          },
        ],
      };

      this.memberOptions = {
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
    fillTeamChartData() {
      let labels = [];
      let data = [];
      let backgroundColors = [];
      let suggestedMax;
      let suggestedMin;
      let max = 0;
      let min = 0;
      let index = 0;

      for (const earning of this.earnings_by_team) {
        labels.push(earning.team_name);
        data.push(earning.cost);
        index = index + 1;
        if (earning.cost > max) {
          max = earning.cost;
        }

        if (earning.cost < min) {
          min = earning.cost;
        }

        if (earning.cost >= window.constants.team_top_threshold) {
          backgroundColors.push(window.chartColors.green);
        } else if (earning.cost >= window.constants.team_intermediate_threshold) {
          backgroundColors.push(window.chartColors.blue);
        } else if (earning.cost >= window.constants.team_elementary_threshold) {
          backgroundColors.push(window.chartColors.orange);
        } else if (earning.cost >= window.constants.team_last_threshold) {
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
    fillYearChartData() {
      let labels = [];
      let data = [];
      let backgroundColors = [];
      let suggestedMax;
      let suggestedMin;
      let max = 0;
      let min = 0;

      for (const earning of this.earnings_by_year) {
        labels.push(earning.year + '.' + earning.month);
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

      this.yearChartData = {
        labels: labels,
        datasets: [
          {
            backgroundColor: backgroundColors,
            label: NumberUtil.currencyFormatter(this.summary_year),
            data: data,
            fill: false,
          },
        ],
      };

      this.yearOptions = {
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
