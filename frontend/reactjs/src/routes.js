import React from 'react';
import Loadable from 'react-loadable'

import DefaultLayout from './containers/DefaultLayout';

function Loading() {
  return <div>Loading...</div>;
}

const Dashboard = Loadable({
  loader: () => import('./views/Dashboard'),
  loading: Loading,
});

const MyEarning = Loadable({
  loader: () => import('./views/MyEarning'),
  loading: Loading,
});

const TeamEarning = Loadable({
  loader: () => import('./views/TeamEarning'),
  loading: Loading,
});

const CompanyEarning = Loadable({
  loader: () => import('./views/CompanyEarning'),
  loading: Loading,
});

const AccountSetting = Loadable({
  loader: () => import('./views/AccountSetting'),
  loading: Loading,
});

const MyContacts = Loadable({
  loader: () => import('./views/MyContacts'),
  loading: Loading,
});

const MyProjects = Loadable({
  loader: () => import('./views/MyProjects'),
  loading: Loading,
});

const MyEquips = Loadable({
  loader: () => import('./views/MyEquips'),
  loading: Loading,
});

const ManageIncome = Loadable({
  loader: () => import('./views/ManageIncome'),
  loading: Loading,
});

const ManageProjects = Loadable({
  loader: () => import('./views/ManageProjects'),
  loading: Loading,
});

const ManageMembers = Loadable({
  loader: () => import('./views/ManageMembers'),
  loading: Loading,
});
// https://github.com/ReactTraining/react-router/tree/master/packages/react-router-config
const routes = [
  { path: '/', exact: true, name: 'Home', component: DefaultLayout },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/myearning', name: 'MyEarning', component: MyEarning },
  { path: '/teamearning', name: 'TeamEarning', component: TeamEarning },
  { path: '/companyearning', name: 'CompanyEarning', component: CompanyEarning },
  { path: '/accountsetting', name: 'AccountSetting', component: AccountSetting },
  { path: '/mycontacts', name: 'MyContacts', component: MyContacts },
  { path: '/myprojects', name: 'MyProjects', component: MyProjects },
  { path: '/myequips', name: 'MyEquips', component: MyEquips },
  { path: '/manageincome', name: 'ManageIncome', component: ManageIncome },
  { path: '/manageProjects', name: 'ManageProjects', component: ManageProjects },
  { path: '/manageMembers', name: 'ManageMembers', component: ManageMembers },
];

export default routes;
