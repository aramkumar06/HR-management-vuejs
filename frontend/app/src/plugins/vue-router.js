/* ============
 * Vue Router
 * ============
 *
 * The official Router for Vue.js. It deeply integrates with Vue.js core
 * to make building Single Page Applications with Vue.js a breeze.
 *
 * http://router.vuejs.org/en/index.html
 */

import Vue from 'vue';
import VueRouter from 'vue-router';
import routes from '@/routes';
import store from '@/store';

Vue.use(VueRouter);

export const router = new VueRouter({
  routes,
});
router.beforeEach((to, from, next) => {
  if (to.matched.some(m => m.meta.auth) && !store.state.auth.authenticated) {
    /*
     * If the user is not authenticated and visits
     * a page that requires authentication, redirect to the login page
     */
    next({
      name: 'login.index',
    });
  } else if (to.matched.some(m => m.meta.guest) && store.state.auth.authenticated) {
    /*
     * If the user is authenticated and visits
     * an guest page, redirect to the dashboard page
     */
    next({
      name: 'home.index',
    });
  } else if (to.matched.some(m => m.meta.team) && store.state.auth.authenticated) {
    /*
     * If the user is team owner then allows, if a user without permission is trying, rejects it
     */
    if (store.state.auth.user.role_name === 'Officer') {
      next();
    } else {
      next({
        name: 'home.index',
      });
    }
  } else if (to.matched.some(m => m.meta.delegate) && store.state.auth.authenticated) {
    /*
     * If the user is delegate owner then allows, if a user without permission is trying, rejects it
     */
    if (store.state.auth.user.role_name === 'Delegate') {
      next();
    } else {
      next({
        name: 'home.index',
      })
    }
  } else {
    next();
  }
});

Vue.router = router;

export default {
  router,
};
