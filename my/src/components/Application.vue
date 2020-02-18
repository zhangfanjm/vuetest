<template>
  <div >
    {{msg}}
    <el-carousel :interval="4000" type="card" height="600px">
      <el-carousel-item v-for="item in img_list" :key="item">
        <video width="640" height="360" autoplay="autoplay">
          <source :src="item">
        </video>
        <img :src= "item"/>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: 'Application',
  data () {
    return {
      msg: '应用页',
      img_list: [
        /*
        "/static/media/rm.mp4",
        "/static/media/222.png",
        "/static/media/333.png",
        "/static/media/444.jpg",
        "/static/media/555.jpg",
        "/static/media/666.jpg",*/
        //上线部署根目录下静态资源配置
        "./static/media/rm.mp4",
        "./static/media/222.png",
        "./static/media/333.png",
        "./static/media/444.jpg",
        "./static/media/555.jpg",
        "./static/media/666.jpg",
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
