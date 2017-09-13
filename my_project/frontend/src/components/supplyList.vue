<template>
<div>
<el-row type="flex" justify="center">
  <h3>供应商信息列表</h3>
</el-row>
<el-row type="flex" class="secondRow" justify="center">
  <el-table
    ref="singleTable"
    :data="tableData"
    height="500"
    highlight-current-row
    @current-change="handleCurrentChange"
    style="width: 100%">
    <el-table-column
      type="index"
      width="50">
    </el-table-column>
    <el-table-column
      prop="supply_name"
      label="供应商名称"
      width="120">
    </el-table-column>
    <el-table-column
      prop="account_tel"
      label="联系方式"
      width="120">
    </el-table-column>
    <el-table-column
      prop="supply_light"
      label="灯具单价"
      width="120">
    </el-table-column>
    <el-table-column
      prop="supply_furniture"
      label="家具单价"
      width="120">
    </el-table-column>
    <el-table-column
      prop="supply_wood"
      label="木材估量"
      width="120">
    </el-table-column>
    <el-table-column
      property="supply_floor"
      label="地板估量">
    </el-table-column>
 

  </el-table>
</el-row>
</div>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        tableData: [],
        currentRow: null
      }
    },
    created () {
      var self = this
      axios.get('/back/supplyInfo', {})
      .then(function (response) {
        self.tableData = response.data.results
      })
      .catch(e => {
        this.errors.push(e)
      })
      console.log(self.tableData.results)
    },

    methods: {
      setCurrent (row) {
        this.$refs.singleTable.setCurrentRow(row)
      },
      handleCurrentChange (val) {
        this.currentRow = val
      }
    }
  }
</script>
<style scoped>
  .secondRow {
      padding: 50px;
      width: 100%;
      height:100%;
      /*justify: center;*/
  }
 
</style>
