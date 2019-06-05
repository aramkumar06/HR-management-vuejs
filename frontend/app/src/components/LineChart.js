import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  data: () => ({
    chartdata: {
      labels: ['1st week', '2nd week', '3rd week', '4th week'],
      datasets: [
        {
          label: 'Week',
          data: [1250, 1000, 2000, 1500],
          lineTension: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        xAxes: [
          {
            barPercentage: 0.1,
          }
        ],
        yAxes: [
          {
            ticks:
              {
                suggestedMin: 0,
                suggestedMax: 2500
              },
          },
        ],
      }
    }
  }),
  mounted() {
    this.renderChart(this.chartdata, this.options)
  }
}
