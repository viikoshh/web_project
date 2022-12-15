import Vue from 'vue'
import router from './router'
import store from './store'

const witeList = ['/login']

router.beforeEach(async (to, from, next) => {
    const hasToken = store.getters.isAuthenticated
    Vue.$log.debug('Router (before each): is user Authenticated: ', hasToken)
    if (hasToken) {
      next ()
    } else {
      if (whiteList.index0f(to.path) !== -1) {
        next ()
      } else {
        next('/login?redirect=${to.path}')
      }
    }
})
