<template>
  <div id= "User">
    {{page}}
    <br>
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>id</th>
          <th>user</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in user_list" :key="user">
          <td>{{user.pk}}</td>
          <td>{{user.fields.name}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default{
  name: 'User',
  data(){
    return{
      page:'用户页',
      user_list: [],
    }
  },
  created() {
    this.$axios.get("/api/test/")
      .then(response =>{
        console.log(response.data),
        this.django_message = response.data.message
      });
     this.$axios.get("/api/user/")
      .then(response =>{
        console.log(response.data),
        this.user_list = JSON.parse(response.data.data)
      });
  }
}
</script>

<style>
</style>
