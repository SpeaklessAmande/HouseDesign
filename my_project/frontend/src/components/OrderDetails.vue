<template>
  <div class="background">
    <el-row type="flex" justify="center">
      <el-card :body-style="{ padding: '0px' }">
        <img src="../assets/house.jpg" class="picture"></img>
      </el-card>
    </el-row>
    <el-row class="distance" type="flex" justify="space-around">
      <el-col :span="8">
        <el-row>
          <h2>图纸估算价格</h2>
          <el-card>
            <p>灯具价格</p>
            <p>家具价格</p>
            <p>地板价格</p>
            <p>木材价格</p>
            <p>总计估价</p>
          </el-card>
        </el-row>
        <template v-if="user_type == 2">
          <el-row style="margin-top: 28px;">
            <el-steps :center="true" :active="1" finish-status="success">
              <el-step title="已完成"></el-step>
              <el-step title="进行中"></el-step>
              <el-step title="步骤 3"></el-step>
            </el-steps>
          </el-row>
        </template>
        <template v-if="user_type == 1">
          <el-row class="btnPosition" type="flex" justify="space-around">
            <el-col :span="12">
              <el-button class="button" type="warning">参与竞标</el-button>
            </el-col>
          </el-row>
        </template>
        <template v-if="user_type == 2">
          <el-row class="btnPosition" type="flex" justify="space-around">
            <el-col :span="12">
              <el-button class="button" type="success">下一步</el-button>
            </el-col>
          </el-row>
        </template>
      </el-col>
      <el-col :span="8">
        <el-row>
          <template v-if="user_type == 1">
              <h2>选择供应商</h2>
              <el-select style="width: 100%" v-model="value" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
          </template>
          <template v-if="user_type == 2">
            <el-card :body-style="{}">
            </el-card>
          </template>
        </el-row>
        <el-row>
          <template v-if="user_type == 1">
            <h2>图纸实际价格</h2>
            <el-card>
              <p>灯具价格</p>
              <p>家具价格</p>
              <p>地板价格</p>
              <p>木材价格</p>
              <p>装修工费</p>
              <p>总计实价</p>
            </el-card>
          </template>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
      bool: true,
      user_type: 2,
      options: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }],
      value: ''
    }
  },
  computed: {
    clientWidth: function () {
      console.log(document.body.clientWidth)
      return document.body.clientWidth
    }
  }
}
</script>
<style scoped>
.button {
  width: 100%;
  height: 100px;
  font-size: 30px;
  font-weight: bold;
}
.btnPosition {
  margin-top: 28px;
}
p {
  font-weight: bold;
  font-size: 20px;
}
p:not(:last-of-type) {
  margin-bottom: 80px;
}
.distance {
  margin: 30px;
}
.picture {
  width: 100%;
}
.background {
  height: 100%;
  color: #5e6d82;
  background-color: #eee;
}
</style>
