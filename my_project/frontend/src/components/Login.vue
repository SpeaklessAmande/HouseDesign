<template>
  <div  class="background">
    <el-row >
      <el-col :offset="9" :span="6">
        <el-card class="position">
        <el-form :model="form"  >
          <el-form-item index="1" ><img src="../assets/logo.png" width="90" height="90"></el-form-item>
          <el-form-item label="手机号">
            <el-input v-model="form.account" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input type="password" v-model="form.password" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login">提交</el-button>
          </el-form-item>
        </el-form>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    import axios from 'axios'
    export default {
      data () {
        return {
          form: {
            account: '',
            password: ''
          }
        }
      },
      methods: {
        login () {
          var self = this
          axios.post('/back/login/', {
            user_tel: self.form.account,
            user_pas: self.form.password
          }).then(function (response) {
            self.$message('登录成功')
            self.$store.state.user_id = response.data[0]['user_id']
            self.$store.state.user_type = response.data[0]['user_type']
            self.$store.state.user_name = response.data[0]['user_name']
            self.$router.push('/home')
            self.$router.go(1)
          }).catch(e => {
            self.$message('账号或者密码错误，请重新输入')
            this.errors.push(e)
          })
        }
      }
    }
</script>
<style>
.position{
  margin-top:100px;
}
.background{
 background-color:#050304;
 height:100%;
}
</style>

   
