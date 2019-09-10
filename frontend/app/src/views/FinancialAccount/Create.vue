<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <v-layout>
    <v-card contextual-style="dark">
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
                <option v-for="paymentAccount in paymentAccounts" :value="paymentAccount.id">
                  {{ paymentAccount.site_name + ' <' + paymentAccount.account_email + ', ' + paymentAccount.account_first_name + ' ' + paymentAccount.account_last_name + '>' }}
                </option>
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
              Vue.router.push({
                name: 'financial_account.index',
              });
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log(error);
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
              this.paymentAccounts = response.accounts;
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log(error);
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
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log(error);
          })
          .finally(() => {
            this.isLoading = false;
          });
      },
      removeFinancialAccount: function(id, index) {
        this.isLoading = true;
        new FinancialAccountProxy().destroy(id)
          .then((response) => {
            if (response.success == true) {
              this.financialAccounts.slice(index);
            } else {
              console.log(response.message);
            }
          })
          .catch((error) => {
            console.log(error);
          })
          .finally(() => {
            this.isLoading = false;
          });
      }
    },
  }
</script>
