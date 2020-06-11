import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../pages/Login'
import MainFrame from '../pages/MainFrame'
import Dashboard from '../pages/Dashboard'
import ThemeConf from '../pages/siteConfs/ThemeConf'

Vue.use(VueRouter);

// 屏蔽路由的沙比报错
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err);
};
const originalReplace = VueRouter.prototype.replace;
VueRouter.prototype.replace = function replace(location) {
  return originalReplace.call(this, location).catch(err => err);
};

// 注册路由
const routes = [
  {path: '/login', component: Login},
  {
    path: '/', component: MainFrame, children: [
      {path: 'dashboard', component: Dashboard},
      {path: 'siteConfs/ThemeConf', component: ThemeConf},
    ]
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
