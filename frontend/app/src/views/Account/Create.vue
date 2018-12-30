<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Create New Account
      </span>

      <div slot="body">
        <form class="form ">
          <div class="form-group">
            <label>Country</label>
            <select class="form-control" v-model="account.country" required >
              <option v-for="country in $store.state.country.countries" v-bind:value="country.id">{{country.name}}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Site</label>
            <select class="form-control" v-model="account.site" required >
              <option v-for="site in $store.state.site.sites" v-bind:value="site.id">{{site.name}}</option>
            </select>
          </div>
          <div class="form-group">
            <label>First Name</label>
            <input type="input" class="form-control" v-model="account.first_name" required />
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input type="input" class="form-control" v-model="account.last_name" required />
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="input" class="form-control" v-model="account.email" required />
          </div>
          <div class="form-group">
            <label>Email Password</label>
            <input type="input" class="form-control" v-model="account.email_password" required />
          </div>
          <div class="form-group">
            <label>Skype</label>
            <input type="input" class="form-control" v-model="account.skype" required />
          </div>
          <div class="form-group">
            <label>Skype Password</label>
            <input type="input" class="form-control" v-model="account.skype_password" required />
          </div>
          <div class="form-group">
            <label>Phone Number</label>
            <input type="input" class="form-control" v-model="account.phone_number" required />
          </div>
          <div class="form-group">
            <label>Title</label>
            <input type="input" class="form-control" v-model="account.title" required />
          </div>
          <div class="form-group">
            <label>Overview</label>
            <textarea class="form-control" v-model="account.overview" required />
          </div>
          <div class="form-group">
            <label>Recital</label>
            <textarea class="form-control" v-model="account.recital" required />
          </div>
          <div class="form-group">
            <label>Created Date</label>
            <datepicker
              v-model="account.created_date"
              format="yyyy-MM-dd"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <div class="row">
              <div class="col-md-1 offset-md-9">
                <router-link
                  :to="{ name: 'account.index'}"
                  class="btn btn-danger"
                >
                  Cancel
                </router-link>
              </div>
              <div class="col-md-2">
                <button
                  type="button"
                  class="btn btn-success pull-right"
                  :disabled="account.country == null || account.site == null || account.first_name == null || account.last_name == null || account.email == null || account.email_password == null || account.skype == null || account.phone_number == null || account.title == null || account.overview == null || account.recital == null || account.created_date == null"
                  @click="createAccount()"
                >
                  Create Account
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
 * Account Create Page
 * ============
 *
 * Page where the user can create account.
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
  name: 'AccountCreate',

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
      account: {},
    };
  },

  beforeRouteEnter(to, from, next) {
    store.dispatch('country/index');
    store.dispatch('site/index');
    next();
  },

  mounted() {
  },

  methods: {
    createAccount() {
      this.account.created_date = moment(this.account.created_date).format('YYYY-MM-DD');
      this.account.user = this.$store.state.auth.user.id;
      this.$store.dispatch('account/create', this.account);
    },
  },
};
</script>
