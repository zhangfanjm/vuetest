<template>
  <div >
    <el-row >
      <el-col :span="12">
        <div class="grid-content bg-purple">
          <div id="main1" style="width: 100%;height:600px;"></div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="grid-content bg-purple-light">
          <div id="main2" style="width: 100%;height:600px;"></div>
        </div>
      </el-col>
    </el-row>
    <el-row >
      <el-col :span="8">
        <div class="grid-content bg-purple">
          <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
          <div id="main" style="width: 100%;height:600px;"></div>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple-light">
          <div id="main3" style="width: 100%;height:600px;"></div>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">
          <el-calendar v-model="value">
          </el-calendar>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      msg: '首页',
      dataList: [],
      dataList1: [],
      dataName: [],
      tableData: [],

      value: new Date(),

    }
  },
  mounted() {
    this.getData()
    this.init()
    this.init1()
    this.init2()
    this.init3()
  },
  watch:{
    dataList(val){//监听数据发生改变 刷新图表数据
        this.init();
    }
},
  methods:{
    init(){
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.$echarts.init(document.getElementById('main'));

      // 指定图表的配置项和数据
      var option = {
          title: {
              text: 'ECharts 入门示例'
          },
          tooltip: {},
          legend: {
              data:['销量']
          },
          xAxis: {
              data: this.dataName
          },
          yAxis: {},
          series: [{
              name: '销量',
              type: 'bar',
              data: this.dataList
          },
          {
            type: 'line',
            data: this.dataList
          },
          {
            type: 'pie',
            center: ['25%', '30%'],
            radius: '30%',
            data: this.dataList1
          }]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },
    init1(){
      // 基于准备好的dom，初始化echarts实例
              var myChart = this.$echarts.init(document.getElementById('main1'));

              myChart.showLoading();

              var data = {
                  "name": "flare",
                  "children": [
                      {
                          "name": "data",
                          "children": [
                              {
                                   "name": "converters",
                                   "children": [
                                    {"name": "Converters", "value": 721},
                                    {"name": "DelimitedTextConverter", "value": 4294}
                                   ]
                              },
                              {
                                  "name": "DataUtil",
                                  "value": 3322
                              }
                          ]
                      },
                      {
                          "name": "display",
                          "children": [
                              {"name": "DirtySprite", "value": 8833},
                              {"name": "LineSprite", "value": 1732},
                              {"name": "RectSprite", "value": 3623}
                         ]
                      },
                      {
                          "name": "flex",
                          "children": [
                              {"name": "FlareVis", "value": 4116}
                          ]
                      },
                      {
                         "name": "query",
                         "children": [
                          {"name": "AggregateExpression", "value": 1616},
                          {"name": "And", "value": 1027},
                          {"name": "Arithmetic", "value": 3891},
                          {"name": "Average", "value": 891},
                          {"name": "BinaryExpression", "value": 2893},
                          {"name": "Comparison", "value": 5103},
                          {"name": "CompositeExpression", "value": 3677},
                          {"name": "Count", "value": 781},
                          {"name": "DateUtil", "value": 4141},
                          {"name": "Distinct", "value": 933},
                          {"name": "Expression", "value": 5130},
                          {"name": "ExpressionIterator", "value": 3617},
                          {"name": "Fn", "value": 3240},
                          {"name": "If", "value": 2732},
                          {"name": "IsA", "value": 2039},
                          {"name": "Literal", "value": 1214},
                          {"name": "Match", "value": 3748},
                          {"name": "Maximum", "value": 843},
                          {
                           "name": "methods",
                           "children": [
                            {"name": "add", "value": 593},
                            {"name": "and", "value": 330},
                            {"name": "average", "value": 287},
                            {"name": "count", "value": 277},
                            {"name": "distinct", "value": 292},
                            {"name": "div", "value": 595},
                            {"name": "eq", "value": 594},
                            {"name": "fn", "value": 460},
                            {"name": "gt", "value": 603},
                            {"name": "gte", "value": 625},
                            {"name": "iff", "value": 748},
                            {"name": "isa", "value": 461},
                            {"name": "lt", "value": 597},
                            {"name": "lte", "value": 619},
                            {"name": "max", "value": 283},
                            {"name": "min", "value": 283},
                            {"name": "mod", "value": 591},
                            {"name": "mul", "value": 603},
                            {"name": "neq", "value": 599},
                            {"name": "not", "value": 386},
                            {"name": "or", "value": 323},
                            {"name": "orderby", "value": 307},
                            {"name": "range", "value": 772},
                            {"name": "select", "value": 296},
                            {"name": "stddev", "value": 363},
                            {"name": "sub", "value": 600},
                            {"name": "sum", "value": 280},
                            {"name": "update", "value": 307},
                            {"name": "variance", "value": 335},
                            {"name": "where", "value": 299},
                            {"name": "xor", "value": 354},
                            {"name": "_", "value": 264}
                           ]
                          },
                          {"name": "Minimum", "value": 843},
                          {"name": "Not", "value": 1554},
                          {"name": "Or", "value": 970},
                          {"name": "Query", "value": 13896},
                          {"name": "Range", "value": 1594},
                          {"name": "StringUtil", "value": 4130},
                          {"name": "Sum", "value": 791},
                          {"name": "Variable", "value": 1124},
                          {"name": "Variance", "value": 1876},
                          {"name": "Xor", "value": 1101}
                         ]
                        },
                      {
                         "name": "scale",
                         "children": [
                          {"name": "IScaleMap", "value": 2105},
                          {"name": "LinearScale", "value": 1316},
                          {"name": "LogScale", "value": 3151},
                          {"name": "OrdinalScale", "value": 3770},
                          {"name": "QuantileScale", "value": 2435},
                          {"name": "QuantitativeScale", "value": 4839},
                          {"name": "RootScale", "value": 1756},
                          {"name": "Scale", "value": 4268},
                          {"name": "ScaleType", "value": 1821},
                          {"name": "TimeScale", "value": 5833}
                         ]
                      }
                  ]
              };

              var data2 = {
                  "name": "flare",
                  "children": [
                      {
                          "name": "flex",
                          "children": [
                              {"name": "FlareVis", "value": 4116}
                          ]
                      },
                      {
                          "name": "scale",
                          "children": [
                              {"name": "IScaleMap", "value": 2105},
                              {"name": "LinearScale", "value": 1316},
                              {"name": "LogScale", "value": 3151},
                              {"name": "OrdinalScale", "value": 3770},
                              {"name": "QuantileScale", "value": 2435},
                              {"name": "QuantitativeScale", "value": 4839},
                              {"name": "RootScale", "value": 1756},
                              {"name": "Scale", "value": 4268},
                              {"name": "ScaleType", "value": 1821},
                              {"name": "TimeScale", "value": 5833}
                         ]
                      },
                      {
                          "name": "display",
                          "children": [
                              {"name": "DirtySprite", "value": 8833}
                         ]
                      }
                  ]
              };

              myChart.hideLoading();
              var               option = {
                  tooltip: {
                      trigger: 'item',
                      triggerOn: 'mousemove'
                  },
                  legend: {
                      top: '2%',
                      left: '3%',
                      orient: 'vertical',
                      data: [{
                          name: 'tree1',
                          icon: 'rectangle'
                      },
                      {
                          name: 'tree2',
                          icon: 'rectangle'
                      }],
                      borderColor: '#c23531'
                  },
                  series:[
                      {
                          type: 'tree',

                          name: 'tree1',

                          data: [data],

                          top: '5%',
                          left: '7%',
                          bottom: '2%',
                          right: '60%',

                          symbolSize: 7,

                          label: {
                              position: 'left',
                              verticalAlign: 'middle',
                              align: 'right'
                          },

                          leaves: {
                              label: {
                                  position: 'right',
                                  verticalAlign: 'middle',
                                  align: 'left'
                              }
                          },

                          expandAndCollapse: true,

                          animationDuration: 550,
                          animationDurationUpdate: 750

                      },
                      {
                          type: 'tree',
                          name: 'tree2',
                          data: [data2],

                          top: '20%',
                          left: '60%',
                          bottom: '22%',
                          right: '18%',

                          symbolSize: 7,

                          label: {
                              position: 'left',
                              verticalAlign: 'middle',
                              align: 'right'
                          },

                          leaves: {
                              label: {
                                  position: 'right',
                                  verticalAlign: 'middle',
                                  align: 'left'
                              }
                          },

                          expandAndCollapse: true,

                          animationDuration: 550,
                          animationDurationUpdate: 750
                      }
                  ]
              }

              myChart.setOption(option);


    },
    init2(){
      // 基于准备好的dom，初始化echarts实例
              var myChart = this.$echarts.init(document.getElementById('main2'));

              // 指定图表的配置项和数据
              var option = {
                  xAxis: {
                      type: 'category',
                      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: [820, 932, 901, 934, 1290, 1330, 1320],
                      type: 'line',
                      smooth: true
                  }]
              };

              // 使用刚指定的配置项和数据显示图表。
              myChart.setOption(option);
    },
    init3(){
      // 基于准备好的dom，初始化echarts实例
              var myChart = this.$echarts.init(document.getElementById('main3'));

              var data = [{
                  name: 'Apples',
                  value: 70
              }, {
                  name: 'Strawberries',
                  value: 68
              }, {
                  name: 'Bananas',
                  value: 48
              }, {
                  name: 'Oranges',
                  value: 40
              }, {
                  name: 'Pears',
                  value: 32
              }, {
                  name: 'Pineapples',
                  value: 27
              }, {
                  name: 'Grapes',
                  value: 18
              }];

              var option = {
                  title: [{
                      text: 'Pie label alignTo'
                  }, {
                      subtext: 'alignTo: "none" (default)',
                      left: '16.67%',
                      top: '75%',
                      textAlign: 'center'
                  }, {
                      subtext: 'alignTo: "labelLine"',
                      left: '50%',
                      top: '75%',
                      textAlign: 'center'
                  }, {
                      subtext: 'alignTo: "edge"',
                      left: '83.33%',
                      top: '75%',
                      textAlign: 'center'
                  }],
                  series: [{
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: data,
                      animation: false,
                      label: {
                          position: 'outer',
                          alignTo: 'none',
                          bleedMargin: 5
                      },
                      left: 0,
                      right: '66.6667%',
                      top: 0,
                      bottom: 0
                  }, {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: data,
                      animation: false,
                      label: {
                          position: 'outer',
                          alignTo: 'labelLine',
                          bleedMargin: 5
                      },
                      left: '33.3333%',
                      right: '33.3333%',
                      top: 0,
                      bottom: 0
                  }, {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: data,
                      animation: false,
                      label: {
                          position: 'outer',
                          alignTo: 'edge',
                          margin: 20
                      },
                      left: '66.6667%',
                      right: 0,
                      top: 0,
                      bottom: 0
                  }]
              };


              // 使用刚指定的配置项和数据显示图表。
              myChart.setOption(option);
    },
    getData(){
      this.$axios.get("/api/user/")
      .then(res=>{
        console.log(res);
        if(res.data.status == '0'){
          if(res.data.data && res.data.data.length > 0){
            this.tableData = JSON.parse(res.data.data);
            for(var i=0; i<this.tableData.length; i++){
              this.dataList.push(this.tableData[i].pk);
              this.dataName.push(this.tableData[i].fields.name);
              this.dataList1.push({name: this.tableData[i].fields.name, value: this.tableData[i].pk})
            }
          }
        }
      },error=>{
        console.log(error)
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
