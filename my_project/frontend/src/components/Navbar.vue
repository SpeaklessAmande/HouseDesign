<template>
  <el-menu theme="dark" :default-active="'1'" mode="horizontal">
    <el-row type="flex" align="middle" justify="space-between">
      <el-col :span="12">
        <el-menu-item index="1"><img src="../assets/logo.png" width="45" height="45"></el-menu-item>
      </el-col>
      <el-col :span="12">
        <el-menu-item index="3"  style="float: right;" @click="handleLogOut()">注销</el-menu-item>
        <el-submenu index="2" style="float: right;">
          <template slot="title">用户名</template>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
          <el-menu-item index="2-3">选项3</el-menu-item>
        </el-submenu>
      </el-col>
    </el-row>
  </el-menu>
</template>
<script>
export default{
  methods: {
    handleLogOut () {
      console.log('log out!')
    }
  }
}
</script>
<style scoped>
  div{
    width: 100%;
  }
</style>
