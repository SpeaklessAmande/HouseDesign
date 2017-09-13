<template>
<div>


<el-row type="flex" class="secondRow" justify="center">
<el-col :span="6">
    <el-card class="boxCard">
<div slot="header" class="clearfix">
  <span style="line-height: 36px;">流水花销</span>
 
</div>
<div v-for="o in 4" :key="o" class="text item">
  {{'金额往来' + o + ':'+currentFinace[o]}}
</div>
</el-card>
</el-col>
<el-col :span="4">
</el-col>
<el-col  :span="6">
  <div>
  <el-table
    ref="multipleTable"
    :data="tableData3"
    border
    tooltip-effect="dark"
    height="500"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      label="订单名称"
      >
      <template scope="scope">{{ scope.row.date }}</template>
    </el-table-column>
  </el-table>
  <div style="margin-top: 20px">
    <el-button @click="toggleSelection([tableData3[1], tableData3[2]])">查询选择</el-button>
    <el-button @click="toggleSelection()">取消选择</el-button>
  </div>
  </div>
</el-col>
</el-row>
</div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      currentFinace: ['123', '2678', '290', '427', '565'],
      tableData3: [{
        date: '2016-05-03'
      }, {
        date: '2016-05-02'
      }, {
        date: '2016-05-04'
      }, {
        date: '2016-05-01'
      }, {
        date: '2016-05-08'
      }, {
        date: '2016-05-06'
      }, {
        date: '2016-05-07'
      }, {
        date: '2016-05-03'
      }, {
        date: '2016-05-02'
      }, {
        date: '2016-05-04'
      }, {
        date: '2016-05-01'
      }, {
        date: '2016-05-08'
      }, {
        date: '2016-05-06'
      }, {
        date: '2016-05-07'
      }]
    }
  },
  created () {
    var self = this
        // var id = self.$route.params.id;
    axios.get('/test/car/', {})
         .then(function (response) {
           self.table = response.data
           this.$store.state.car_model_id = response.data[0].car_model_id
         })
         .catch(e => {
           this.errors.push(e)
         })
  },
  methods: {
    deleteCar (event) {
      var self = this
      console.log(event)
      axios.post('/test/car/', {
        'statu': 'delete',
        'car_num': [event]
      })
            .then(function (response) {
              self.$message('删除成功')
            })
            .catch(e => {
              self.$message('删除失败')
              this.errors.push(e)
            })
    }
  }
}
</script>
<style scoped>
  .secondRow {
      padding-top: 100px;
      width: 100%;
      /*justify: center;*/
  }
    .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .clearfix:before,
  .clearfix:before {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }

  .boxCard {
    height: 500px;
  }
</style>
