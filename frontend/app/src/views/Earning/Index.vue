<template>
  <v-layout>
    <div class="row">
      <div class="col-md-12">
        <!--<router-link-->
          <!--:to="{ name: 'earning.create' }"-->
          <!--class="btn btn-success pull-right offset-md-10 col-md-2"-->
        <!--&gt;-->
          <!--Add New Earning-->
        <!--</router-link>-->
      </div>
    </div>

    <br />

    <v-card contextual-style="dark">
      <span slot="header">
        My Earnings
      </span>

      <div slot="body">
        <table class="table table-striped">
          <thead>
            <th>
              Site
            </th>
            <th>
              Account
            </th>
            <th>
              Project
            </th>
            <th>
              Client
            </th>
            <th>
              Week
            </th>
            <th>
              Cost
            </th>
            <th>
              Status
            </th>
          </thead>
          <tbody>
            <tr v-for="earning in $store.state.earning.earnings">
              <td>
                {{ earning.site_name }}
              </td>
              <td>
                {{ earning.account_first_name + ' ' + earning.account_last_name }}
              </td>
              <td>
                {{ earning.project_title }}
              </td>
              <td>
                {{ earning.client_first_name + ' ' + earning.client_last_name }}
              </td>
              <td>
                {{ earning.year }}-{{ earning.week_of_year }}
              </td>
              <td>
                {{ earning.cost }}
              </td>
              <td>
                {{ earning.status }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </v-card>

  </v-layout>
</template>

<script>
import VLayout from '@/layouts/Default.vue';
import VCard from '@/components/Card.vue';
import store from '@/store';

export default {
  /**
   * The name of the page.
   */
  name: 'EarningIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
  },

  beforeRouteEnter(to, from, next) {
    /**
     * expected query parameter
     *   project_id
     *   week
     *   month
     *   year
     */
    store.dispatch('earning/index', to.query)
      .then((response) => {
        if (response.success === true) {
          store.commit('earning/INDEX', response.earnings);
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
};
</script>
