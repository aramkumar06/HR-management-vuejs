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

    // Only delegate owner can view this page
    meta: {
      delegate: true,
    },
  },

  // Approval Earning Update
  {
    path: '/approval/:earning_id/update',
    name: 'approval.update',
    component: () => import('@/views/Approval/Update.vue'),

    // Only delegate owner can view this page
    meta: {
      delegate: true,
    },
  },

  // Financial Account Index
  {
    path: '/financial_accounts',
    name: 'financial_account.index',
    component: () => import('@/views/FinancialAccount/Index.vue'),

    // Only delegate owner can view this page
    meta: {
      delegate: true,
    },
  },

  // Financial Account Create
  {
    path: '/financial_accounts/create',
    name: 'financial_account.create',
    component: () => import('@/views/FinancialAccount/Create.vue'),

    // Only delegate owner can view this page
    meta: {
      delegate: true,
    },
  },

  // Reward Index Create
  {
    path: '/rewards/create',
    name: 'reward.index',
    component: () => import('@/views/Reward/Index.vue'),

    // Only delegate owner can view this page
    meta: {
      delegate: true,
    },
  },

  // Report Index
  {
    path: '/report',
    name: 'report.index',
    component: () => import('@/views/Report/Index.vue'),

    // Only delegate owner can view this page
    meta: {
      delegate: true,
    },
  },

  // Profile Update
  {
    path: '/profile',
    name: 'profile.update',
    component: () => import('@/views/Profile/Update.vue'),

    // If the user needs to be authenticated to view this page.
    meta: {
      auth: true,
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
