<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
      </span>

      <div slot="body">
        <form class="form">
          <div class="form-group">
            <label>Status</label>
            <select
              class="form-control"
              v-model="earning.status"
            >
              <option v-for="status in $store.state.earning.earningStatuses" :value="status.value">
                {{ status.caption }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label>Account</label>
            <select
              class="form-control"
              v-model="earning.account"
            >
              <option v-for="account in $store.state.account.accounts" :value="account.id">
                {{ account.account_first_name + ' ' + account.account_last_name + '<' + account.account_email +'>' }}
              </option>
            </select>
          </div>
          <div class="form-group" v-if="earning.status == 'Withdraw'">
            <label>Created Date</label>
            <datepicker
              format="yyyy-MM-dd"
              class="form-control"
              v-model="earning.withdrawn_date"
              required />
          </div>
          <div class="form-group">
            <label>Cost</label>
            <input
              type="number"
              step="0.01"
              class="form-control"
              v-model="earning.cost"
            />
          </div>
          <div class="form-group">
            <div class="row">
              <div class="col-md-1 offset-md-9">
                <router-link
                  :to="{ name: 'earning.index'}"
                  class="btn btn-danger"
                >
                  Cancel
                </router-link>
              </div>
              <div class="col-md-2">
                <button
                  type="button"
                  class="btn btn-success pull-right"
                  :disabled="earning.week === null || earning.cost === null || earning.status === null || earning.account == null"
                  @click="createEarning()"
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
  /* ============
   * Earning Input Page
   * ============
   *
   * Page where the user can input earning.
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
    name: 'EarningCreate',

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
        earning: {},
      };
    },
    beforeRouteEnter(to, from, next) {
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
    computed: {
    },
    methods: {
      createEarning() {
        if (this.earning.status == 'Withdraw' && (this.earning.withdrawn_date == undefined || this.earning.withdrawn_date == null)) {
          return;

          console.log('Withdraw date omitted');
        }

        this.earning.earned_by = this.$store.state.auth.user.id;

        this.$store.dispatch('earning/create', this.earning);
      },
    },
  };
</script>
