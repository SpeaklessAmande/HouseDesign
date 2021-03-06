import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Hello from '../components/Hello.vue'
import Login from '../components/Login.vue'
import Navbar from '../components/Navbar.vue'
import OrderDetails from '../components/OrderDetails.vue'
import supplyList from '../components/supplyList.vue'
import boundList from '../components/boundList.vue'
import blueprintList from '../components/blueprintList.vue'
import newOrder from '../components/newOrder.vue'
export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      components: {
        top: Navbar,
        default: Hello
      }
    },
    {
      path: '/order/:id',
      components: {
        top: Navbar,
        default: OrderDetails
      }
    },
    {
      path: '/supplyList',
      components: {
        top: Navbar,
        default: supplyList
      }
    },
    {
      path: '/boundList',
      components: {
        top: Navbar,
        default: boundList
      }
    },
    {
      path: '/blueprintList',
      components: {
        top: Navbar,
        default: blueprintList
      }
    },
    {
      path: '/newOrder',
      components: {
        top: Navbar,
        default: newOrder
      }
    }
  ]
})
