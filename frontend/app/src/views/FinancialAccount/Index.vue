<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="info">
      <span slot="header">
        Financial Account and Emails Mapping
      </span>

      <div slot="body">
        <div v-if="!isLoading">
          <div class="row mb-5">
            <div class="col-5">
              <router-link
                :to="{ name: 'financial_account.create' }"
                class="btn btn-success"
              >
                Add New Mapping
              </router-link>
            </div>
            <div class="col-6">
              <select
                class="form-control"
                v-model="filterObject.financial_account_id"
                >
                <option label=""></option>
                <optgroup v-for="(optGroup, key) in paymentAccounts" :label="key">
                  <option v-for="account in optGroup" :value="account.id">
                    {{ account.account_first_name + ' ' + account.account_last_name + '<' + account.account_email +'>' }}
                  </option>
                </optgroup>
              </select>
            </div>
            <div class="col-1">
              <button
                class="btn btn-xs btn-primary pull-right"
                @click="getFinancialAccounts()"
              >
                Filter
              </button>
            </div>
          </div><!-- end of filter div-->
          <div class="row">
            <table class="table">
              <thead>
                <th>
                  Financial Account
                </th>
                <th>
                  Email
                </th>
                <th>
                  Owner
                </th>
                <th></th>
              </thead>
              <tbody>
                <tr v-for="(financialAccount, index) in financialAccounts">
                  <td>{{ financialAccount.finance_site_name + ' (' + financialAccount.finance_first_name + ' ' + financialAccount.finance_last_name + ')' }}</td>
                  <td>{{ financialAccount.account_email }}</td>
                  <td>{{ financialAccount.owner_last_name + ' ' + financialAccount.owner_first_name }}</td>
                  <td>
                    <button
                      class="btn btn-sm btn-danger"
                      @click="removeFinancialAccount(financialAccount.id, index)"
                    >
                      Remove
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div><!-- end of listing div -->
        </div>

        <div class="loading-parent">
          <loading
            :active.sync="isLoading"
            :can-cancel=false
            :is-full-page=true />
        </div>
      </div>

      <span slot="footer"></span>
    </v-card>
  </v-layout>
</template>

<script>
  /* ============
  * Financial Account Index Page
  * ============
  *
  * The financial account index page
  */

  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import store from '@/store';
  import AccountProxy from '@/proxies/AccountProxy.js';
  import FinancialAccountProxy from '@/proxies/FinancialAccountProxy.js';
  import BasicUtil from '@/utils/BasicUtil.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'FinancialAccountIndex',

    /**
     * The components that the page can use.
     */
    components: {
      Loading,
      VLayout,
      VCard,
    },
    data() {
      return {
        isLoading: false,
        filterObject: {
          financial_account_id: null,
        },
        paymentAccounts: [],
        financialAccounts: [],
      };
    },
    mounted() {
      this.getPaymentAccounts();
      this.getFinancialAccounts();
    },
    computed: {},
    methods: {
      getPaymentAccounts: function() {
        this.isLoading = true;
        new AccountProxy().payments()
          .then((response) => {
            if (response.success == true) {
              this.paymentAccounts = BasicUtil.buildOptGroup(response.accounts, 'site_name');
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
      getFinancialAccounts: function() {
        this.isLoading = true;
        new FinancialAccountProxy(this.filterObject).all()
          .then((response) => {
            if (response.success == true) {
              this.financialAccounts = response.accounts;
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
      removeFinancialAccount: function(id, index) {
        new FinancialAccountProxy().destroy(id)
          .then((response) => {
            if (response.success == true) {
              this.financialAccounts.splice(index, 1);
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
      }
    },
  }
</script>
