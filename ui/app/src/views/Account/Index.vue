<template>
  <v-layout>

    <div class="row">
      <div class="col-md-12">
        <router-link
          :to="{ name: 'account.create' }"
          class="btn btn-success pull-right offset-md-10 col-md-2"
        >
          Add New Account
        </router-link>
      </div>
    </div>

    <br />

    <v-card contextual-style="dark">
      <span slot="header">
        My Accounts
      </span>
      <div slot="body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>
                Country
              </th>
              <th>
                Site
              </th>
              <th>
                Name
              </th>
              <th>
                Email
              </th>
              <th>
                Status
              </th>
              <th />
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="account in $store.state.account.accounts">
              <td>
                {{ account.country_name }}
              </td>
              <td>
                {{ account.site_name }}
              </td>
              <td>
                {{ account.account_first_name }} {{ account.account_last_name }}
              </td>
              <td>
                {{ account.account_email }}
              </td>
              <td>
                <strong v-if="account.account_status">
                  Active
                </strong>
                <strong v-if="!account.account_status">
                  Not Active
                </strong>
              </td>
              <th>
                <button class="btn btn-xs btn-primary">
                  Projects
                  <i class="fa fa-arrow-right" />
                </button>
              </th>
              <th>
                <router-link
                  :to="{name: 'account.update', params: {account_id: account.account_id}}"
                  class="btn btn-xs btn-info">
                  Edit
                </router-link>
              </th>
            </tr>
          </tbody>
        </table>
      </div>
      <div slot="footer">
        Made by abc
      </div>
    </v-card>
  </v-layout>
</template>

<script>
/* ============
 * Account Index Page
 * ============
 *
 * Page where the user can view the accounts information.
 */

import VLayout from '@/layouts/Default.vue';
import VCard from '@/components/Card.vue';

export default {
  /**
   * The name of the page.
   */
  name: 'AccountIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
  },

  mounted() {
    this.$store.dispatch('account/index');
  },
};
</script>
