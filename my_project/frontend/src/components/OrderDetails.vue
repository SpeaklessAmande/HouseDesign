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
            <p>灯具价格：<span>{{ light_price }}</span></p>
            <p>家具价格：<span>{{ furniture_price }}</span></p>
            <p>地板价格：<span>{{ floor_price }}</span></p>
            <p>木材价格：<span>{{ wood_price }}</span></p>
            <p>总计估价：<span>{{ total_price }}</span></p>
          </el-card>
        </el-row>
        <template v-if="$store.state.user_type == 'account'">
          <el-row style="margin-top: 28px;">
            <el-steps :center="true" :active="node_number" finish-status="success">
              <el-step title="招标阶段"></el-step>
              <el-step title="施工阶段"></el-step>
              <el-step title="验收阶段"></el-step>
            </el-steps>
          </el-row>
        </template>
        <template v-if="$store.state.user_type == 'contractor'">
          <el-row class="btnPosition" type="flex" justify="space-around">
            <el-col :span="12">
              <el-button class="button" type="warning" @click="submit_bid">参与竞标</el-button>
            </el-col>
          </el-row>
        </template>
        <template v-if="$store.state.user_type == 'account'">
          <el-row class="btnPosition" type="flex" justify="space-around">
            <el-col :span="12">
              <el-button class="button" type="success" @click="submit_log">下一步</el-button>
            </el-col>
          </el-row>
        </template>
      </el-col>
      <el-col :span="8">
        <el-row>
          <template v-if="$store.state.user_type == 'contractor'">
              <h2>选择供应商</h2>
              <el-col :span="20">
              <el-select style="width: 100%" v-model="selected_supply" placeholder="请选择">
                <el-option
                  v-for="item in supplys"
                  :key="item.supply_id"
                  :label="item.supply_name"
                  :value="item.supply_id">
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
              <div v-for="comment in comments">
                <el-row>
                  <el-col :span="10" :offset="comment.user_type == $store.state.user_type ? 14 : 0">
                    <span style="font-weight: bold">{{ comment.comment_name }}:</span>
                    <el-card>{{ comment.comment_content }}</el-card>
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
                    v-model="comment_input">
                  </el-input>
                </el-col>
                <el-col :span="4" :offset="2">
                  <el-button @click="submit_comment" style="height: 100%; width: 100%"type="success">发送</el-button>
                </el-col>
              </el-row>
            </el-card>
          </template>
        </el-row>
        <el-row>
          <template v-if="$store.state.user_type == 'contractor'">
            <h2>图纸实际价格</h2>
            <el-card>
              <p>灯具价格：<span>{{  }}</span></p>
              <p>家具价格：<span>{{  }}</span></p>
              <p>地板价格：<span>{{  }}</span></p>
              <p>木材价格：<span>{{  }}</span></p>
              <p>装修工费：<span>{{  }}</span></p>
              <p>总计实价：<span>{{  }}</span></p>
            </el-card>
          </template>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  data () {
    return {
      supplys: [],
      build: {},
      node_number: 1,
      comments: [],
      comment_input: '',
      selected_supply: {}
    }
  },
  methods: {
    submit_comment () {
      var self = this
      // need certain URL
      if (self.comment_input.length === 0) {
        self.$message('输入不能为空')
      } else {
        axios.post('/back/comment/', {
          comment_content: self.comment_input,
          comment_build_id: self.$route.params.id,
          comment_user_id: self.$store.state.user_id
        }).then(function (response) {
          self.$message('评论成功')
          if (self.comments.length >= 6) {
            self.comments.shift()
          }
          self.comments.push({user_type: self.$store.state.user_type, comment_name: self.$store.state.user_name, comment_content: self.comment_input})
        }).catch(e => {
          self.$message('评论失败')
          this.errors.push(e)
        })
      }
    },
    submit_bid () {
      var self = this
      // need certain URL
      if (self.selected_supply.length === 0) {
        self.$message('请选择一个供应商')
      } else {
        axios.post('/back/bid/', {
          bid_build_id: self.$route.params.id,
          bid_supply_id: self.selected_supply,
          bid_contractor_id: self.$store.state.user_id
        }).then(function (response) {
          self.$message('竞标成功')
        }).catch(e => {
          self.$message('竞标失败')
          this.errors.push(e)
        })
      }
    },
    submit_log () {
      var self = this
      // need certain URL
      axios.post('/back/confirm/', {
        build_id: self.$route.params.id,
        node_number: self.node_number
      }).then(function (response) {
        self.$message('确认成功')
      }).catch(e => {
        self.$message('确认失败')
        this.errors.push(e)
      })
    }
  },
  computed: {
    wood_price () {
      return this.build['build_wood'] * this.build['build_wood_price']
    },
    light_price () {
      return this.build['build_light'] * this.build['build_light_price']
    },
    floor_price () {
      return this.build['build_floor'] * this.build['build_floor_price']
    },
    furniture_price () {
      return this.build['build_furniture'] * this.build['build_furniture_price']
    },
    total_price () {
      return this.wood_price + this.light_price + this.floor_price + this.furniture_price
    },
    actual_wood_price () {
      return this.build['build_wood'] * this.selected_supply['supply_wood']
    },
    actual_light_price () {
      return this.build['build_light'] * this.selected_supply['supply_light']
    },
    actual_floor_price () {
      return this.build['build_floor'] * this.selected_supply['supply_floor']
    },
    actual_furniture_price () {
      return this.build['build_furniture'] * this.selected_supply['supply_furniture']
    },
    actual_total_price () {
      return this.actual_wood_price + this.actual_light_price + this.actual_floor_price + this.actual_furniture_price
    }
  },
  created () {
    var self = this
    axios.post('/back/blueprint/', {
      user_type: self.$store.state.user_type,
      user_id: self.$store.state.user_id,
      build_id: Number(self.$route.params.id)
    }).then(function (response) {
      console.log('blueprint created')
      if (self.$store.state.user_type === 'account') {
        self.node_number = response.data[0]
        self.comments = response.data[1]
        self.build = response.data[2]
      } else if (self.$store.state.user_type === 'designer') {
        self.comments = response.data[0]
        self.build = response.data[1]
      } else if (self.$store.state.user_type === 'contractor') {
        self.supplys = response.data[0]
        self.build = response.data[1]
      }
    }).catch(e => {
      console.log(e)
      self.$message('cant get anything')
      self.errors.push(e)
    })
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
