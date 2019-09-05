<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
      </span>

      <div slot="body">
        <div
          class="row"
          v-if="!isLoading"
        >
          <div class="col-12">
            <form class="form">
              <div class="form-group">
                <label>Withdrawn Date</label>
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
                  <div class="col-1 offset-9">
                    <router-link
                      :to="{ name: 'approval.index'}"
                      class="btn btn-danger"
                    >
                      Cancel
                    </router-link>
                  </div>
                  <div class="col-2">
                    <button
                      type="button"
                      class="btn btn-success pull-right"
                      :disabled="earning.cost === null"
                      @click="updateEarning()"
                    >
                      Update
                    </button>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="loading-parent">
          <loading
            :active.sync="isLoading"
            :can-cancel=false
            :is-full-page=true />
        </div>
      </div>
    </v-card>
  </v-layout>
</template>

<script>
  /* ============
   * Earning Update Page
   * ============
   *
   * Page where the user can update earning.
   */
  import Vue from 'vue';
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import Datepicker from 'vuejs-datepicker';
  import moment from 'moment';
  import store from '@/store';
  import UserProxy from '@/proxies/UserProxy.js';
  import AccountProxy from '@/proxies/AccountProxy.js';
  import EarningProxy from '@/proxies/EarningProxy.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'EarningUpdate',

    /**
     * The components that the page can use.
     */
    components: {
      Loading,
      VLayout,
      VCard,
      Datepicker,
    },
    data() {
      return {
        isLoading: false,
        earning: {
          cost: null,
          status: null,
          account: null,
        },
        earned_by_me: true,
        users: [],
        accounts: [],
      };
    },
    mounted() {
      this.fetchEarning();
      this.fetchCommonAccounts();
      this.fetchDelegationMembers();
    },
    computed: {
    },
    methods: {
      updateEarning() {
        if (this.earning.withdrawn_date == undefined || this.earning.withdrawn_date == null) {
          return;

          console.log('Withdraw date omitted');
        }

        this.earning.year = moment(this.earning.withdrawn_date).year();
        this.earning.withdrawn_date = moment(this.earning.withdrawn_date).format('YYYY-MM-DD');

        const earning_id = this.earning['id'];
        delete this.earning['id'];

        const params = {
          id: earning_id,
          data: this.earning
        };

        this.$store.dispatch('earning/update', params);
      },
      fetchDelegationMembers() {
        this.isLoading = true;
        new UserProxy().index()
          .then((response) => {
            if (response.success == true) {
              this.users = response.users;
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log('Request failed...');
          })
          .finally(() => {
            this.isLoading = false;
          });
      },
      fetchCommonAccounts() {
        this.isLoading = true;
        new AccountProxy().with_common()
          .then((response) => {
            if (response.success == true) {
              this.accounts = response.accounts;
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log('Request failed...');
          })
          .finally(() => {
            this.isLoading = false;
          });
      },
      fetchEarning() {
        const earning_id = this.$route.params.earning_id;
        this.isLoading = true;
        new EarningProxy().find(earning_id)
          .then((response) => {
            if (response.success == true) {
              this.earning = response.earning;
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log('Request failed...');
          })
          .finally(() => {
            this.isLoading = false;
          });
      },
    },
  };
</script>
