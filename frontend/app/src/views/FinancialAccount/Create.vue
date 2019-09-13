<template xmlns:v-on="http://www.w3.org/1999/xhtml">
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
            <div
              class="form-group"
            >
              <label>Payment Account</label>
              <select
                class="form-control"
                v-model="financial_account.account_finance_id"
                >
                <optgroup v-for="(optGroup, key) in paymentAccounts" :label="key">
                  <option v-for="account in optGroup" :value="account.id">
                    {{ account.account_first_name + ' ' + account.account_last_name + '<' + account.account_email +'>' }}
                  </option>
                </optgroup>
              </select>
            </div><!-- end of payment account -->
            <div class="form-group">
              <label>Email</label>
              <select
                class="form-control"
                v-model="financial_account.account_email_id"
              >
                <option v-for="freelancingAccount in freelancingAccounts" :value="freelancingAccount.id">
                  {{ freelancingAccount.site_name + ' <' + freelancingAccount.account_email + ', ' + freelancingAccount.account_first_name + ' ' + freelancingAccount.account_last_name + '>' }}
                </option>
              </select>
            </div><!-- end of email account -->
            <div class="form-group">
              <div class="row">
                <div class="col-md-1 offset-md-9">
                  <router-link
                    :to="{ name: 'financial_account.index'}"
                    class="btn btn-danger"
                  >
                    Cancel
                  </router-link>
                </div>
                <div class="col-md-2">
                  <button
                    type="button"
                    class="btn btn-success pull-right"
                    :disabled="financial_account.account_finance_id === null || financial_account.account_email_id === null"
                    @click="createMapping()"
                  >
                    Save
                  </button>
                </div>
              </div>
            </div><!-- end of actions -->
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
   * Financial Account Create Page
   * ============
   *
   * Page where the admin can register financial account mapping.
   */

  import Vue from 'vue';
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import AccountProxy from '@/proxies/AccountProxy.js';
  import FinancialAccountProxy from '@/proxies/FinancialAccountProxy.js';
  import BasicUtil from '@/utils/BasicUtil.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'FinancialAccountCreate',

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
        financial_account: {
          account_finance_id: null,
          account_email_id: null,
        },
        paymentAccounts: [],
        freelancingAccounts: [],
      };
    },
    mounted() {
      this.getPaymentAccounts();
      this.getFreelanceAccounts();
    },
    computed: {},
    methods: {
      createMapping: function() {
        this.isLoading = true;
        new FinancialAccountProxy().create(this.financial_account)
          .then((response) => {
            if (response.success == true) {
              this.$notify({
                group: 'notify',
                type: 'success',
                title: 'Success',
                text: response.message,
                duration: 3000,
                speed: 1000,
              });
              Vue.router.push({
                name: 'financial_account.index',
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
      getFreelanceAccounts: function() {
        this.isLoading = true;
        new AccountProxy().freelancing_accounts()
          .then((response) => {
            if (response.success == true) {
              this.freelancingAccounts = response.accounts;
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
  }
</script>
