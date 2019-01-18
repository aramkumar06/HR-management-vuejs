<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Create New Project
      </span>

      <div slot="body">
        <form class="form">
          <div class="form-group">
            <label>Account</label>
            <select class="form-control" v-model="project.account" required >
              <option v-for="account in $store.state.account.accounts" v-bind:value="account.id">{{ account.account_first_name + ' ' +  account.account_last_name }}</option>
            </select>
          </div>
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
            <input type="input" class="form-control" v-model="project.description" required />
          </div>
          <div class="form-group">
            <label>Start Date</label>
            <input type="input" class="form-control" v-model="project.start_date" />
          </div>
          <div class="form-group">
            <label>End Date</label>
            <input type="input" class="form-control" v-model="project.end_date" />
          </div>
          <div class="form-group">
            <label>Status</label>
            <input type="input" class="form-control" v-model="project.status" />
          </div>
          <div class="form-group">
            <label>Project Type</label>
            <input type="input" class="form-control" v-model="project.project_type" />
          </div>
          <div class="form-group">
            <label>Price</label>
            <input type="input" class="form-control" v-model="project.price" />
          </div>
          <div class="form-group">
            <label>Limit</label>
            <input type="input" class="form-control" v-model="client.recital" />
          </div>
          <div class="form-group">
            <label>Posted DateTime</label>
            <input type="input" class="form-control" v-model="client.recital" />
          </div>
          <div class="form-group">
            <label>Applied DateTime</label>
            <datepicker v-model="client.recital" class="form-control" />
          </div>
          <div class="form-group">
            <label>Applied Proposals Count</label>
            <input type="input" class="form-control" v-model="client.recital" />
          </div>
          <div class="form-group">
            <label>Interview Count</label>
            <input type="input" class="form-control" v-model="client.recital" />
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
      client: {},
    };
  },

  beforeRouteEnter(to, from, next) {
    store.dispatch('account/index');
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
      this.client.user = this.$store.state.auth.user.id;
      this.$store.dispatch('project/create', this.project);
    },
  },
};
</script>
