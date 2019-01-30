<template>
  <v-layout>
    <div class="row">
      <div class="col-md-12">
        <router-link
          :to="{ name: 'earning.create' }"
          class="btn btn-success pull-right offset-md-10 col-md-2"
        >
          Add New Earning
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
                {{ earning.client_first_name + ' ' + earining.client_last_name }}
              </td>
              <td>
                {{ earning.week }}
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
