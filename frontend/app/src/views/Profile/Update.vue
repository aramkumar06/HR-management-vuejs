<template>
  <v-layout>
    <v-card contextual-style="dark">
      <span slot="header">
      </span>

      <div slot="body">
        <div
          class="row"
          v-if="!isLoading">
          <div class="col-12">
            <form class="form">
              <div class="form-group">
                <label class="label">Password</label>
                <input
                  type="password"
                  class="form-control"
                  v-model="user.password" />
              </div>
              <div class="form-group">
                <label class="label">Password Confirmation</label>
                <input
                  type="password"
                  class="form-control"
                  v-model="user.password_confirmation" />
              </div>
              <div class="form-group">
                <div class="row">
                  <div class="col-1 offset-9">
                    <router-link
                      :to="{ name: 'home.index' }"
                      class="btn btn-danger">
                      Cancel
                    </router-link>
                  </div>
                  <div class="col-2">
                    <button
                      type="button"
                      class="btn btn-success pull-right"
                      :disabled="user.password == null || user.password == '' || user.password != user.password_confirmation "
                      @click="updateProfile()"
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
   * Profile Update Page
   * ============
   *
   * Page where the user can update his profile.
   */
  import Vue from 'vue';
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import VLayout from '@/layouts/Default.vue';
  import VCard from '@/components/Card.vue';
  import store from '@/store';
  import UserProxy from '@/proxies/UserProxy.js';

  export default {
    /**
     * The name of the page.
     */
    name: 'ProfileUpdate',

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
        user: {
          password: null,
          password_confirmation: null,
        }
      }
    },
    mounted() {},
    computed: {},
    methods: {
      updateProfile() {
        this.isLoading = true;
        new UserProxy().update(this.$store.state.auth.user.id, this.user)
          .then((response) => {
            if (response.success == true) {
              this.$store.dispatch('auth/logout');
            }
          })
          .catch((error) => {
            console.log("Error occurs while updating");
          })
          .finally(() => {
            this.isLoading = false;
          });
      },
    }
  };
</script>
