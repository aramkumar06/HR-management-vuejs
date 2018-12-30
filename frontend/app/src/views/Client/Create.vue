<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Create New Client
      </span>

      <div slot="body">
        <form class="form">
          <div class="form-group">
            <label>Country</label>
            <select class="form-control" v-model="client.country" required >
              <option v-for="country in $store.state.country.countries" v-bind:value="country.id">{{ country.name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Site</label>
            <select class="form-control" v-model="client.site" required >
              <option v-for="site in $store.state.site.sites" v-bind:value="site.id">{{ site.name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Account</label>
            <select class="form-control" v-model="client.account" required >
              <option v-for="account in $store.state.account.accounts" v-bind:value="account.id">{{ account.account_first_name + ' ' +  account.account_last_name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>First Name</label>
            <input type="input" class="form-control" v-model="client.first_name" required />
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input type="input" class="form-control" v-model="client.last_name" required />
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="input" class="form-control" v-model="client.email" />
          </div>
          <div class="form-group">
            <label>Skype</label>
            <input type="input" class="form-control" v-model="client.skype" />
          </div>
          <div class="form-group">
            <label>Phone Number</label>
            <input type="input" class="form-control" v-model="client.phone_number" />
          </div>
          <div class="form-group">
            <label>Url</label>
            <input type="input" class="form-control" v-model="client.url" />
          </div>
          <div class="form-group">
            <label>Recital</label>
            <input type="input" class="form-control" v-model="client.recital" />
          </div>
          <div class="form-group">
            <div class="row">
              <div class="col-md-1 offset-md-9">
                <router-link
                  :to="{ name: 'client.index'}"
                  class="btn btn-danger"
                >
                  Cancel
                </router-link>
              </div>
              <div class="col-md-2">
                <button
                  type="button"
                  class="btn btn-success pull-right"
                  :disabled="client.country == null || client.site == null || client.account == null || client.first_name == null || client.last_name == null"
                  @click="createClient()"
                >
                  Create Client
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
 * Client Create Page
 * ============
 *
 * Page where the user can create client.
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
  name: 'ClientCreate',

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
    store.dispatch('country/index');
    store.dispatch('site/index');
    store.dispatch('account/index')
      .then((response) => {
        if (response.success === true) {
          store.commit('account/INDEX', response.accounts);
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
    createClient() {
      this.client.created_date = moment(this.client.created_date).format('YYYY-MM-DD');
      this.client.user = this.$store.state.auth.user.id;
      this.$store.dispatch('client/create', this.client);
    },
  },
};
</script>
