<template>

<el-row class="singlerow">
  <el-col :span="6" v-for="(o,index) in 6" :key="o" :offset="index%3 > 0 ? 3 : 0" class="blueprint">
    <el-card :body-style="{ padding: '0px' }">
      <router-link :to="'/order/'+ o" >
        <img src="../assets/logo.png"  class="image">
      </router-link>
      <div>
        <div class="bottom clearfix">
          
          <el-button v-if="$store.state.user_type=='account'" type="text" class="button">参与竞标</el-button>
          <time class="time">{{ currentDate }}</time>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>

</template>

<style>
  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
  .blueprint {
    padding: 30px;
  }
</style>

<script>
export default {
  data () {
    return {
      currentDate: new Date()
    }
  }
}
</script>
