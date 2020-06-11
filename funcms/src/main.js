import Vue from 'vue'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import './plugins/element.js'
import router from './router'

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');

Vue.use(VueCookies);
