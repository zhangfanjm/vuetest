<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <div>
          <el-menu
            router
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose">
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span>首页</span>
              </template>
              <el-menu-item index="/index">首页</el-menu-item>
              <el-menu-item index="/video">视频</el-menu-item>
            </el-submenu>
            <el-menu-item index="/application">
              <i class="el-icon-menu"></i>
              <span slot="title">应用管理</span>
            </el-menu-item>
            <el-menu-item index="/user" >
              <i class="el-icon-document"></i>
              <span slot="title">用户管理</span>
            </el-menu-item>
            <el-submenu index="4">
              <template slot="title">
                <i class="el-icon-setting"></i>
                <span slot="title">配置管理</span>
              </template>
              <el-menu-item index="/config">配置1</el-menu-item>
              <el-menu-item index="4-2">配置2</el-menu-item>
            </el-submenu>
          </el-menu>
        </div>
      </el-aside>
      <el-container>
        <el-header>{{msg}}</el-header>
        <el-main><router-view/></el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
