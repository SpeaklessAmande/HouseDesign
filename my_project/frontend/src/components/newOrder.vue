<template>
  <div>
      <el-row type="flex" justify="center">
          <h2>添加订单</h2>
          </el-row>
      <el-row type="flex" justify="center">
          <el-form :model="ruleForm" label-width="100px">
            <el-form-item label="订单名称">
            <el-input placeholder="请输入内容" v-model="formInline.build_name" >
            </el-input>
            </el-form-item>
            <el-form-item label="账户ID">
            <el-input placeholder="请输入内容" v-model="formInline.build_account_id" >
            </el-input>
            </el-form-item>
            <el-form-item label="设计师">
            <el-input placeholder="请输入内容" v-model="formInline.build_designer" >

            </el-input>
            </el-form-item>
            <el-form-item label="蓝图URL">
            <el-input placeholder="请输入内容" v-model="formInline.build_blueprint" >

            </el-input>
            </el-form-item>
            <el-form-item label="设计费">
            <el-input placeholder="请输入内容" v-model="formInline.build_blueprint_price" >

            </el-input>
            </el-form-item>
            <el-form-item label="创建时间">
                    <el-date-picker
      v-model="formInline.build_date"
      type="date"
      :picker-options="pickerOptions0">
    </el-date-picker>

            </el-input>
            </el-form-item>
            <el-form-item label="木材估量">
            <el-input placeholder="请输入内容" v-model="formInline.build_wood" >

            </el-input>
            </el-form-item>
            <el-form-item label="灯具估量">
            <el-input placeholder="请输入内容" v-model="formInline.build_light" >

            </el-input>
            </el-form-item>
            <el-form-item label="地板估量">
            <el-input placeholder="请输入内容" v-model="formInline.build_floor" >
               
            </el-input>
            </el-form-item>
            <el-form-item label="地板估量">
            <el-input placeholder="请输入内容" v-model="formInline.build_furniture" >
                  
            </el-input>
            </el-form-item>
            </el-form>
       
      </el-row>
      <el-row type="flex" justify="center">
        
          <el-button type="primary" @click="addCar">提交</el-button>
     
      </el-row>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  data () {
    return {
      formInline: {
        build_name: '',
        build_account_id: '',
        build_designer: '',
        build_blueprint: '',
        build_blueprint_price: '',
        build_date: '',
        build_wood: '',
        build_light: '',
        build_floor: '',
        build_furniture: ''
      }
    }
  },
  methods: {
    addCar () {
      var self = this
      console.log(self.form.account)
      axios.post('/back/order/', {
        build_name: self.formInline.build_name,
        build_account_id: self.formInline.build_account_id,
        build_designer: self.formInline.build_designer,
        build_blueprint: self.formInline.build_blueprint,
        build_blueprint_price: self.formInline.build_blueprint_price,
        build_date: self.formInline.build_date,
        build_wood: self.formInline.build_wood,
        build_light: self.formInline.build_light,
        build_floor: self.formInline.build_floor,
        build_furniture: self.formInline.build_furniture
      })
            .then(function (response) {
              self.$message('添加成功')
            })
            .catch(e => {
              self.$message('添加失败')
              this.errors.push(e)
            })
    }
  }
}
</script>
<style scoped>
.text{
  font-size: 5px;
  color:grey;
}
</style>
