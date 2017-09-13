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
      property="date"
      label="供应商名称"
      width="120">
    </el-table-column>
    <el-table-column
      property="name"
      label="联系方式"
      width="120">
    </el-table-column>
    <el-table-column
      property="address"
      label="灯具单价"
      width="240">
    </el-table-column>
    <el-table-column
      property="addres"
      label="家具单价">
    </el-table-column>
 

  </el-table>
</el-row>
</div>
</template>

<script>
  export default {
    data () {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          addres: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄',
          addres: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄',
          addres: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄',
          addres: '上海市普陀区金沙江路 1518 弄'
        }],
        currentRow: null
      }
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
