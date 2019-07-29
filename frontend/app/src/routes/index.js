/* ============
 * Routes File
 * ============
 *
 * The routes and redirects are defined in this file.
 */

export default [
  // Home
  {
    path: '/home',
    name: 'home.index',
    component: () => import('@/views/Home/Index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },

  // Account Index
  {
    path: '/account',
    name: 'account.index',
    component: () => import('@/views/Account/Index.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
    },
  },

  // Account Create
  {
    path: '/account/create',
    name: 'account.create',
    component: () => import('@/views/Account/Create.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
    },
  },

  // Account Update
  {
    path: '/account/:account_id/update',
    name: 'account.update',
    component: () => import('@/views/Account/Update.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
    },
  },

  // Earning Index
  {
    path: '/earning',
    name: 'earning.index',
    component: () => import('@/views/Earning/Index.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
    },
  },

  // Earning Create
  {
    path: '/earning/create',
    name: 'earning.create',
    component: () => import('@/views/Earning/Create.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
    },
  },

  // Earning Update
  {
    path: '/earning/:earning_id/update',
    name: 'earning.update',
    component: () => import('@/views/Earning/Update.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
    },
  },

  // Approval Index
  {
    path: '/approval',
    name: 'approval.index',
    component: () => import('@/views/Approval/Index.vue'),

    // Only team owner can view this page
    meta: {
      team: true,
    },
  },

  // Login
  {
    path: '/login',
    name: 'login.index',
    component: () => import('@/views/Login/Index.vue'),

    // If the user needs to be a guest to view this page.
    meta: {
      guest: false,
    },
  },

  // Register
  {
    path: '/register',
    name: 'register.index',
    component: () => import('@/views/Register/Index.vue'),

    // If the user needs to be a guest to view this page.
    meta: {
      guest: false,
    },
  },

  {
    path: '/',
    redirect: '/home',
  },

  {
    path: '/*',
    redirect: '/home',
  },
];
