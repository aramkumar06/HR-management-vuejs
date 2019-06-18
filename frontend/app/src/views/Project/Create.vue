<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Create New Project
      </span>

      <div slot="body">
        <form class="form">
          <div class="form-group">
            <label>Client</label>
            <select class="form-control" v-model="project.client" required >
              <option v-for="client in $store.state.client.clients" v-bind:value="client.id">{{ client.client_first_name + ' ' + client.client_last_name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Title</label>
            <input type="input" class="form-control" v-model="project.title" required />
          </div>
          <div class="form-group">
            <label>Description</label>
            <textarea class="form-control" v-model="project.description" required />
          </div>
          <div class="form-group">
            <label>Start Date</label>
            <datepicker v-model="project.start_date" />
          </div>
          <div class="form-group">
            <label>End Date</label>
            <datepicker v-model="project.end_date" />
          </div>
          <div class="form-group">
            <label>Status</label>
            <select v-model="project.status" class="form-control">
              <option v-for="status in $store.state.project.statuses" v-bind:value="status.key">{{ status.value }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Project Type</label>
            <select v-model="project.project_type" class="form-control">
              <option v-for="projectType in $store.state.project.projectTypes" v-bind:value="projectType.key">{{ projectType.value }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Price</label>
            <input type="input" class="form-control" v-model="project.price" />
          </div>
          <div class="form-group">
            <label>Limit</label>
            <input type="input" class="form-control" v-model="project.limit" />
          </div>
          <div class="form-group">
            <label>Posted DateTime</label>
            <datepicker v-model="project.posted_datetime" />
          </div>
          <div class="form-group">
            <label>Applied DateTime</label>
            <datepicker v-model="project.applied_datetime" />
          </div>
          <div class="form-group">
            <label>Applied Proposals Count</label>
            <input type="input" class="form-control" v-model="project.applied_proposals_count" />
          </div>
          <div class="form-group">
            <label>Interview Count</label>
            <input type="input" class="form-control" v-model="project.interview_count" />
          </div>
          <div class="form-group">
            <div class="row">
              <div class="col-md-1 offset-md-9">
                <router-link
                  :to="{ name: 'project.index'}"
                  class="btn btn-danger"
                >
                  Cancel
                </router-link>
              </div>
              <div class="col-md-2">
                <button
                  type="button"
                  class="btn btn-success pull-right"
                  :disabled="project.account == null || project.client == null || project.title == null || project.description == null || project.status == null"
                  @click="createProject()"
                >
                  Create Project
                </button>
              </div>
            </div>
          </div>
        </form>
      </div><!-- end of body -->

      <div slot="footer">
        Made by abc
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
  name: 'ProjectCreate',

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
      project: {},
    };
  },

  beforeRouteEnter(to, from, next) {
    store.dispatch('client/index')
      .then((response) => {
        if (response.success === true) {
          store.commit('client/INDEX', response.clients);
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
    createProject() {
      this.project.user_in_charge = this.$store.state.auth.user.id;
      /*
       * TODO
       * should add validation whether start_date is before end date
       * should add validation whether posted_datetime is before applied_datetime
       */
      if (this.project.start_date) {
        this.project.start_date = moment(this.project.start_date).format('YYYY-MM-DD');
      }

      if (this.project.end_date) {
        this.project.end_date = moment(this.project.end_date).format('YYYY-MM-DD');
      }

      if (this.project.posted_datetime) {
        this.project.posted_datetime = moment(this.project.posted_datetime).format('YYYY-MM-DDT00:00');
      }

      if (this.project.applied_datetime) {
        this.project.applied_datetime = moment(this.project.applied_datetime).format('YYYY-MM-DDThh:00');
      }

      this.$store.dispatch('project/create', this.project);
    },
  },
};
</script>
