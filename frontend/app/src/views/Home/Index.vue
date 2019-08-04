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
            <v-line-chart
              v-if="memberEarningsLoaded"
              :chart-data="memberChartData"
              :options="memberOptions"
            ></v-line-chart>
          </div>
          <div class="col-6">
            <v-line-chart
              v-if="teamEarningsLoaded"
              :chart-data="teamChartData"
              :options="teamOptions"
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
import VLineChart from '@/components/LineChart.js';
import '@/utils/ColorUtil.js';

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
      summary_member: null,
      summary_team: null,
      memberChartData: null,
      teamChartData: null,
      memberOptions: null,
      teamOptions: null,
      memberEarningsLoaded: false,
      teamEarningsLoaded: false,
    }
  },
  mounted() {
    this.getReportByMember();
    this.getReportByTeam();
  },
  methods: {
    getReportByMember() {
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
            this.memberEarningsLoaded = true;
            this.fillMemberChartData();
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
            this.teamEarningsLoaded = true;
            this.fillTeamChartData();
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
    fillMemberChartData() {
      let labels = [];
      let data = [];
      let backgroundColors = [];
      let suggestedMax;
      let suggestedMin;
      let max = 0;
      let min = 0;
      let index = 0;
      const multiplier = 1.5;
      const top_threshold = 2500;
      const intermediate_threshold = 2000;
      const elementary__threshold = 1500;
      const last_threshold = 500;

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

        if (earning.cost >= top_threshold) {
          backgroundColors.push(window.chartColors.green);
        } else if (earning.cost >= intermediate_threshold) {
          backgroundColors.push(window.chartColors.blue);
        } else if (earning.cost >= elementary__threshold) {
          backgroundColors.push(window.chartColors.orange);
        } else if (earning.cost >= last_threshold) {
          backgroundColors.push(window.chartColors.yellow);
        } else {
          backgroundColors.push(window.chartColors.red);
        }
      }

      suggestedMax = max * multiplier;
      suggestedMin = min * multiplier;

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
      const multiplier = 1.5;
      const top_threshold = 2500;
      const intermediate_threshold = 2000;
      const elementary__threshold = 1500;
      const last_threshold = 500;

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

        if (earning.cost >= top_threshold) {
          backgroundColors.push(window.chartColors.green);
        } else if (earning.cost >= intermediate_threshold) {
          backgroundColors.push(window.chartColors.blue);
        } else if (earning.cost >= elementary__threshold) {
          backgroundColors.push(window.chartColors.orange);
        } else if (earning.cost >= last_threshold) {
          backgroundColors.push(window.chartColors.yellow);
        } else {
          backgroundColors.push(window.chartColors.red);
        }
      }

      suggestedMax = max * multiplier;
      suggestedMin = min * multiplier;

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
  }
};
</script>
