<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
        Update Account
      </span>

      <div slot="body">
        <form class="col-12 form">
          <div class="form-group">
            <label>Country</label>
            <select
              v-model="account.country"
              class="form-control"
              required >
              <option v-for="country in $store.state.country.countries" v-bind:value="country.id">{{country.name}}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Site</label>
            <select
              v-model="account.site"
              class="form-control"
              required >
              <option v-for="site in $store.state.site.sites" v-bind:value="site.id">{{site.name}}</option>
            </select>
          </div>
          <div class="form-group">
            <label>First Name</label>
            <input
              v-model="account.first_name"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input
              v-model="account.last_name"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Email</label>
            <input
              v-model="account.email"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Email Password</label>
            <input
              v-model="account.email_password"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Skype</label>
            <input
              v-model="account.skype"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Skype Password</label>
            <input
              v-model="account.skype_password"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Phone Number</label>
            <input
              v-model="account.phone_number"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Title</label>
            <input
              v-model="account.title"
              type="input"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Overview</label>
            <textarea
              v-model="account.overview"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Recital</label>
            <textarea
              v-model="account.recital"
              class="form-control"
              required />
          </div>
          <div class="form-group">
            <label>Created Date</label>
            <datepicker
              v-model="account.created_date"
              format="yyyy-MM-dd"
              class="form-control"
              required />
          </div>
          <!--<div class="form-group">-->
            <!--<label>Is Payment Account?</label>-->
            <!--<input-->
              <!--type="checkbox"-->
              <!--v-model="account.is_payment_account"-->
              <!--required-->
            <!--/>-->
          <!--</div>-->
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
                  :disabled="account.country == null || account.site == null || account.first_name == null || account.last_name == null || account.email == null || account.email_password == null || account.skype == null || account.phone_number == null || account.title == null || account.overview == null || account.recital == null || account.created_date == null"
                  type="button"
                  class="btn btn-success pull-right"
                  @click="updateAccount()"
                >
                  Update Account
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>

      <div slot="footer">
        Made by abc
      </div>
    </v-card>
  </v-layout>
</template>

<script>
/* ============
 * Account Update Page
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
  name: 'AccountUpdate',

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
      account: this.$store.state.account.account,
    };
  },

  beforeRouteEnter(to, from, next) {
    store.dispatch('country/index');
    store.dispatch('site/index');
    store.dispatch('account/find', to.params.account_id)
      .then((response) => {
        if (response.success === true) {
          store.commit('account/FIND', response.account);
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
    updateAccount() {
      this.account.created_date = moment(this.account.created_date).format('YYYY-MM-DD');
      this.account.user = this.$store.state.auth.user.id;
      const payload = {
        id: this.$route.params.account_id,
        data: this.account,
      };
      this.$store.dispatch('account/update', payload);
    },
  },
};
</script>
