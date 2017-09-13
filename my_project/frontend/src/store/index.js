import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// root state object.
// each Vuex instance is just a single state tree.
const state = {
  // 用户ID
  user_id: 132,
  // 用户类型
  user_type: 'account',
  // 用户名称
  user_name: 'Kenny'
}
    // mutations are operations that actually mutates the state.
    // each mutation handler gets the entire state tree as the
    // first argument, followed by additional payload arguments.
    // mutations must be synchronous and can be recorded by plugins
    // for debugging purposes.
const mutations = {
}

// actions are functions that causes side effects and can involve
// asynchronous operations.
const actions = {
}

// getters are functions
const getters = {
}

// A Vuex instance is created by combining the state, mutations, actions,
// and getters.
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
