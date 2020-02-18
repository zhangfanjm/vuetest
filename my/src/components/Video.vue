<template>
  <div >
    {{msg}}
    <el-row>
      <el-col :span="12">
        <div class="grid-content bg-purple">
          <video width="640" height="360" autoplay="autoplay">
            <source :src="video_list">
          </video>
        </div>
      </el-col>
      <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'vedio',
  data () {
    return {
      msg: 'Welcome to vedio',
      video_list: [
        //"/static/media/rm.mp4",
        "./static/media/rm.mp4",    //上线部署根目录下静态资源配置
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
