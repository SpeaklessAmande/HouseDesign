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
        <template v-if="$store.state.user_type == 'account'">
          <el-row style="margin-top: 28px;">
            <el-steps :center="true" :active="1" finish-status="success">
              <el-step title="已完成"></el-step>
              <el-step title="进行中"></el-step>
              <el-step title="步骤 3"></el-step>
            </el-steps>
          </el-row>
        </template>
        <template v-if="$store.state.user_type == 'contractor'">
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
          <template v-if="$store.state.user_type == 'contractor'">
              <h2>选择供应商</h2>
              <el-col :span="20">
              <el-select style="width: 100%" v-model="value" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              </el-col>
              <el-col :span="4">
                <el-button style="width: 100%" type="warning">详情</el-button>
              </el-col>
          </template>
          <template v-if="$store.state.user_type == 'designer' || $store.state.user_type == 'account'">
            <h2>与您的<span v-if="$store.state.user_type == 'account'">设计师</span><span v-if="$store.state.user_type == 'designer'">客户</span>交流</h2>
            <el-card>
              <div style="height: 550px;">
              <div v-for="item in items">
                <el-row>
                  <el-col :span="10" :offset="item.user_type == $store.state.user_type ? 14 : 0">
                    <span style="font-weight: bold">{{ item.user_id }}:</span>
                    <el-card>{{ item.message }}</el-card>
                  </el-col>
                </el-row>
              </div>
              </div>
              <el-row class="btnPosition">
                <el-col :span="18">
                  <el-input
                    type="textarea"
                    :autosize="{ minRows: 1, maxRows: 4}"
                    placeholder="请输入内容"
                    v-model="textarea3">
                  </el-input>
                </el-col>
                <el-col :span="4" :offset="2">
                  <el-button style="height: 100%; width: 100%"type="success">发送</el-button>
                </el-col>
              </el-row>
            </el-card>
          </template>
        </el-row>
        <el-row>
          <template v-if="$store.state.user_type == 'contractor'">
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
      items: [
      { user_type: 'account', user_id: 'ID2', message: 'Foo' },
      { user_type: 'designer', user_id: 'ID3', message: 'Bar' },
      { user_type: 'account', user_id: 'ID2', message: 'hafuhafu' },
      { user_type: 'designer', user_id: 'ID3', message: 'Bar' },
      { user_type: 'designer', user_id: 'ID3', message: 'Bar' },
      { user_type: 'designer', user_id: 'ID3', message: 'Bar' },
      { user_type: 'designer', user_id: 'ID3', message: 'Bar' }
      ],
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
