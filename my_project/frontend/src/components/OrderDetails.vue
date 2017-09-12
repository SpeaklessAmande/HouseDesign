<template>
  <div class="background">
    <el-row type="flex" justify="center">
      <el-card :body-style="{ padding: '0px' }">
        <img src="../assets/house.jpg" class="picture"></img>
      </el-card>
    </el-row>
    <el-row v-if="" class="distance" type="flex" justify="space-around">
      <el-col :span="8">
        <el-card style="height: 80px">
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card style="height: 80px">
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if-else="">
    </el-row>
    <el-row v-else="">
    </el-row>
  </div>
</template>
<script>
export default{
  data () {
    return {
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
.distance {
  margin: 30px;
}
.picture {
  width: 100%;
}
.background {
  height: 100%;
  background-color: #eee;
}
</style>
