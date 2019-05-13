<template>
  <v-layout>
    <div class="row">
      <div class="col-md-12">
        <router-link
          :to="{ name: 'project.create' }"
          class="btn btn-success pull-right offset-md-10 col-md-2"
        >
          Add New Project
        </router-link>
      </div>
    </div>

    <br />

    <v-card contextual-style="dark">
      <span slot="header">
        My Projects
      </span>
      <div slot="body">
        <table class="table table-striped">
          <thead>
            <th>
              Title
            </th>
            <th>
              Start Date
            </th>
            <th>
              Project Type
            </th>
            <th>
              Status
            </th>
            <th>
              Client
            </th>
            <th>
              Account
            </th>
            <th>
              Site
            </th>
            <th></th>
            <th></th>
          </thead>
          <tbody>
            <tr v-for="project in $store.state.project.projects">
              <td>
                {{ project.title }}
              </td>
              <td>
                {{ project.start_date }}
              </td>
              <td>
                {{ project.project_type }}
              </td>
              <td>
                {{ project.status }}
              </td>
              <td>
                {{ project.client_first_name + ' ' + project.client_last_name }}
              </td>
              <td>
                {{ project.account_first_name + ' ' + project.account_last_name }}
              </td>
              <td>
                {{ project.site_name }}
              </td>
              <td>
                <router-link
                  :to="{name: 'earning.create', params: {project_id: project.id}}"
                  class="btn btn-xs btn-primary"
                >
                  Add Earnings
                  <i class="fa fa-arrow-right" />
                </router-link>
              </td>
              <td>
                <router-link
                  :to="{name: 'project.update', params: {project_id: project.id}}"
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
  name: 'ProjectIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VCard,
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
};
</script>
