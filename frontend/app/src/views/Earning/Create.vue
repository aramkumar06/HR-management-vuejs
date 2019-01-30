<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">

      </span>

      <div slot="body">
        <form class="form">
          <div class="form-group">
            <label>Project</label>
            <select class="form-control" v-model="earning.project" required>
              <option v-for="project in $store.state.project.projects" v-bind:value="project.id">{{ project.title }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Start Week Date</label>
            <datepicker v-model="earning.start_week_date"></datepicker>
          </div>
          <div class="form-group">
            <label>End Week Date</label>
            <datepicker v-model="earning.end_week_date"></datepicker>
          </div>
          <div class="form-group">
            <label>Week Of Year</label>
            <input type="input" class="form-control" v-model="earning.week_of_year" />
          </div>
          <div class="form-group">
            <label>Month Of Year</label>
            <input type="input" class="form-control" v-model="earning.month_of_year" />
          </div>
          <div class="form-group">
            <label>Year</label>
            <input type="input" class="form-control" v-model="earning.year" />
          </div>
          <div class="form-group">
            <div class="row">
              <div class="col-md-1 offset-md-9">
                <router-link
                  :to="{ name: 'earning.index'}"
                  class="btn btn-danger"
                >
                  Cancel
                </router-link>
              </div>
              <div class="col-md-2">
                <button
                  type="button"
                  class="btn btn-success pull-right"
                  :disabled="earning.project == null || earning.start_week_date == null || earning.end_week_date == null || earning.week_of_year == null || earning.month_of_year == null || earning.year == null"
                  @click="createEarning()"
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
/* ============
 * Project Create Page
 * ============
 *
 * Page where the user can create project.
 */

import VLayout from '@/layouts/Default.vue';
import VCard from '@/components/Card.vue';
import Datepicker from 'vuejs-datepicker';
import moment from 'moment';
import store from '@/store';

export default {
  /**
   * The name of the page.
   */
  name: 'EarningCreate',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
    Datepicker,
  },

  data() {
    return {
      earning: {},
    };
  },

  beforeRouteEnter(to, from, next) {
    store.dispatch('project/index')
      .then((response) => {
        if (response.success === true) {
          store.commit('project/INDEX', response.projects);
          next();
        } else {
          console.log('Request failed...');
        }
      })
      .catch(() => {
        console.log('Request failed...');
      });
  },

  mounted() {
  },

  methods: {
    createEarning() {
      if (this.earning.start_week_date) {
        this.earning.start_week_date = moment(this.earning.start_week_date).format('YYYY-MM-DD');
      }

      if (this.earning.end_week_date) {
        this.earning.end_week_date = moment(this.earning.end_week_date).format('YYYY-MM-DD');
      }

      this.$store.dispatch('earning/create', this.earning);
    },
  },
};
</script>
