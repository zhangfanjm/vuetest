<template>
  <div >
    <el-button @click="resetDateFilter">清除日期过滤器</el-button>
      <el-button @click="clearFilter">清除所有过滤器</el-button>
      <el-table
        v-loading="loading"
        ref="filterTable"
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="pk"
          label="日期"
          sortable
          width="180"
          column-key="date"
          :filters="dataList"
          :filter-method="filterHandler"
        >
        </el-table-column>
        <el-table-column
          prop="fields.name"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="model"
          label="地址"
          :formatter="formatter">
        </el-table-column>
        <el-table-column
          prop="pk"
          label="标签"
          width="100"
          :filters="dataList"
          :filter-method="filterTag"
          filter-placement="bottom-end">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.pk === 1 ? 'primary' : 'success'"
              disable-transitions>{{scope.row.pk}}</el-tag>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        class="page"
        background
        layout="prev, pager, next"
        :current-page.sync="currentPage"
        page-size = 3
        :total="tableData.length">
      </el-pagination>
  </div>
</template>

<script>
export default {
  name: 'Config',
  data () {
    return {
      dataList: [],
      tableData: [],
      pageSize : 3
    }
  },
  mounted() {
    this.getData();
  },
  computed:{
    nowTableData(){
      return this.tableData.slice((this.currentPage-1)*this.pageSize,this.currentPage*this.pageSize);
    }
  },
  methods: {
    getData(){
      this.loading = true;
      this.$axios.get("/api/user/")
      .then(res=>{
        console.log(res);
        if(res.data.status == '0'){
          if(res.data.data && res.data.data.length > 0){
            this.tableData = JSON.parse(res.data.data);
            for(var i=0; i<this.tableData.length; i++){
              this.dataList.push({text: this.tableData[i].pk, value: this.tableData[i].pk})
            }
            this.loading = false;
          }
        }
      },error=>{
        console.log(error)
      });
    },
    resetDateFilter() {
      this.$refs.filterTable.clearFilter('date');
    },
    clearFilter() {
      this.$refs.filterTable.clearFilter();
    },
    formatter(row, column) {
      return row.model;
    },
    filterTag(value, row) {
      return row.pk === value;
    },
    filterHandler(value, row, column) {
      const property = column['property'];
      return row[property] === value;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.page{
  margin-top: 20px;
}
</style>
