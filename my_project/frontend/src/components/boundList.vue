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
    :data="tableData"
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
      <template scope="scope">{{ scope.row.build_name }}</template>
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
      tableData: []
    }
  },
  created () {
    var self = this
    // var load = {'user_id': '1'}
    axios.get('/back/userCost/1', {'user_id': '1'})
         .then(function (response) {
           self.tableData = response.data
         })
         .catch(e => {
           this.errors.push(e)
         })
  },
  methods: {
    // deleteCar (event) {
    //   var self = this
    //   console.log(event)
    //   axios.post('/test/car/', {
    //     'statu': 'delete',
    //     'car_num': [event]
    //   })
    //         .then(function (response) {
    //           self.$message('删除成功')
    //         })
    //         .catch(e => {
    //           self.$message('删除失败')
    //           this.errors.push(e)
    //         })
    // }
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
