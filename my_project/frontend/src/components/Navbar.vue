<template>
  <el-menu theme="dark" :default-active="'1'" mode="horizontal">
    <el-row type="flex" align="middle" justify="space-between">
      <el-col :span="12">
        <el-menu-item index="1"><img src="../assets/logo.png" width="45" height="45"></el-menu-item>
      </el-col>
      <el-col :span="12">
        <el-menu-item index="3"  style="float: right;" @click="handleLogOut()">注销</el-menu-item>
        <el-submenu index="2" style="float: right;">
          <template slot="title">{{ $store.state.user_name }}</template>
          <el-menu-item index="2-1" v-if="$store.state.user_type == 'designer'">新增订单</el-menu-item>
          <el-menu-item index="2-2" v-if="$store.state.user_type == 'contractor'">参与竞标</el-menu-item>
          <el-menu-item index="2-3">账户明细</el-menu-item>
        </el-submenu>
      </el-col>
    </el-row>
  </el-menu>
</template>
<script>
export default{
  methods: {
    handleLogOut () {
      this.$router.push('/')
      this.$router.go(1)
    }
  }
}
</script>
<style scoped>
  div{
    width: 100%;
  }
</style>
