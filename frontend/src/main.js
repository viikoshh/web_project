import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'
// import './plugins/vue.logger'
// import './plugins/vue.notificatons'
// import './plugins/api.service'
// import './auth.control'
// import axios
import axios from 'axios'

// set a prototype for http
Vue.prototype.$http = axios;

import Default from '@/layouts/Default.vue'
import Centered from '@/layouts/Centered.vue'

Vue.component('default-layout', Default)
Vue.component('centered-layout', Centered)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')