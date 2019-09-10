<template>
  <div id="app">
    <router-view/>

    <notifications group="notify" position="bottom right" />
  </div>
</template>
<script>
/* ============
 * Entry Point
 * ============
 *
 * The entry point of the application.
 */

export default {
  /**
   * The name of the application.
   */
  name: 'Portal',

  /**
   * Fires when the app has been mounted.
   */
  mounted() {
    // If the user is authenticated,
    // fetch the data from the API
    if (this.$store.state.auth.authenticated) {
      // comment
      // this.$store.dispatch('account/find');
    }
  },
};
</script>
