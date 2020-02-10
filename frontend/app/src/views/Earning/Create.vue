<template>
  <v-layout>
    <v-card contextual-style="info">
      <span slot="header">
      </span>

      <div slot="body">
        <div
          class="row"
          v-if="!isLoading"
        >
          <form class="col-12 form">
            <div class="form-group">
              <input type="checkbox" v-model="earned_by_me" />
              <label>Earned by me?</label>
            </div>
            <div
              class="form-group"
              v-if="earned_by_me == false"
            >
              <label>Earned by</label>
              <select
                class="form-control"
                v-model="earning.earned_by"
                >
                <option v-for="user in users" :value="user.id">
                  {{ user.name }} <{{ user.username }}>
                </option>
              </select>
            </div>
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
                <optgroup v-for="(optGroup, key) in accounts" :label="key">
                  <option v-for="account in optGroup" :value="account.id">
                    {{ account.account_first_name + ' ' + account.account_last_name + '<' + account.account_email +'>' }}
                  </option>
                </optgroup>
              </select>
            </div>
            <div class="form-group">
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
              <label>Comments</label>
              <input
                type="text"
                class="form-control"
                v-model="earning.comments"
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
                    :disabled="earning.cost === null || earning.status === null || earning.account == null"
                    @click="createEarning()"
                  >
                    Save
                  </button>
                </div>
              </div>
            </div>
          </form>
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
   * Earning Input Page
   * ============
   *
   * Page where the user can input earning.
   */

  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import Datepicker from 'vuejs-datepicker';
  import moment from 'moment';
  import store from '@/store';
  import UserProxy from '@/proxies/UserProxy.js';
  import AccountProxy from '@/proxies/AccountProxy.js';
  import BasicUtil from '@/utils/BasicUtil.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'EarningCreate',

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
      this.fetchCommonAccounts();
      this.fetchDelegationMembers();
    },
    computed: {
    },
    methods: {
      createEarning() {
        if (this.earning.status === 'Withdraw' && (this.earning.withdrawn_date === undefined || this.earning.withdrawn_date === null)) {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Error occurred',
            text: 'Withdraw date omitted',
            duration: 3000,
            speed: 1000,
          });

          return;
        }

        if (this.earned_by_me === false && (this.earning.earned_by === "undefined" || this.earning.earned_by === null)) {
          this.$notify({
            group: 'notify',
            type: 'error',
            title: 'Error occurred',
            text: 'Please select earned by',
            duration: 3000,
            speed: 1000,
          });
        }

        if (this.earned_by_me === true) {
          this.earning.earned_by = this.$store.state.auth.user.id;
        }

        this.earning.year = store.state.auth.app.active_year;
        this.earning.withdrawn_date = moment(this.earning.withdrawn_date).format('YYYY-MM-DD');

        this.$store.dispatch('earning/create', this.earning);
      },
      fetchDelegationMembers() {
        this.isLoading = true;
        new UserProxy().index()
          .then((response) => {
            if (response.success === true) {
              this.users = response.users;
              this.$notify({
                group: 'notify',
                type: 'success',
                title: 'Success',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            } else {
              this.$notify({
                group: 'notify',
                type: 'error',
                title: 'Error occurred',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            }
          })
          .catch(() => {
	          this.$notify({
	            group: 'notify',
	            type: 'error',
	            title: 'Error occurred',
	            text: 'Something went wrong',
	            duration: 3000,
	            speed: 1000,
	          });
          })
          .finally(() => {
            this.isLoading = false;
          });
      },

      fetchCommonAccounts() {
        this.isLoading = true;
        new AccountProxy().with_common()
          .then((response) => {
            if (response.success === true) {
              this.accounts = BasicUtil.buildOptGroup(response.accounts, 'site_name');
              console.log(this.accounts);
              this.$notify({
                group: 'notify',
                type: 'success',
                title: 'Success',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            } else {
              this.$notify({
                group: 'notify',
                type: 'error',
                title: 'Error occurred',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
            }
          })
          .catch(() => {
            this.$notify({
		          group: 'notify',
		          type: 'error',
		          title: 'Error occurred',
		          text: 'Something went wrong',
		          duration: 3000,
		          speed: 1000,
		        });
          })
          .finally(() => {
            this.isLoading = false;
          });
      },
    },
  };
</script>
