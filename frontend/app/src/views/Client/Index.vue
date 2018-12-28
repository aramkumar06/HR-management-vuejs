<template>
  <v-layout>
    <div class="row">
      <div class="col-md-12">
        <router-link
          :to="{ name: 'client.create' }"
          class="btn btn-success pull-right offset-md-10 col-md-2"
        >
          Add New Client
        </router-link>
      </div>
    </div>

    <br />

    <v-card contextual-style="dark">
      <span slot="header">
        My Clients
      </span>
      <div slot="body">
        <table class="table table-striped">
          <thead>
            <th>
              Country
            </th>
            <th>
              Account Name
            </th>
            <th>
              Client Name
            </th>
            <th>
              Registered Date
            </th>
            <th>
              Projects
            </th>
            <th>
              Edit
            </th>
          </thead>
          <tbody>
            <tr v-for="client in clients">
              <td>
                {{ client.country_name }}
              </td>
              <td>
                {{ client.account_name }}
              </td>
              <td>
                {{ client.client_name }}
              </td>
              <td>
                {{ client.registed_date }}
              </td>
              <td>
                <button class="btn btn-xs btn-primary">
                  Projects
                  <i class="fa fa-arrow-right" />
                </button>
              </td>
              <td>
                <router-link
                  :to="{name: 'client.update', params: {client_id: client.client_id}}"
                  class="btn btn-xs btn-info">
                  Edit
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div><!-- end of body -->

      <div slot="footer">
        Made by abc
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
  name: 'AccountIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
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
};
</script>
