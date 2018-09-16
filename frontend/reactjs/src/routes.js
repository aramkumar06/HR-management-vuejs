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

// https://github.com/ReactTraining/react-router/tree/master/packages/react-router-config
const routes = [
  { path: '/', exact: true, name: 'Home', component: DefaultLayout },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/myearning', name: 'MyEarning', component: MyEarning },
  { path: '/teamearning', name: 'TeamEarning', component: TeamEarning },
];

export default routes;
