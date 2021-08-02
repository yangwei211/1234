<template>
  <div>
    <v-data-table :headers="headers" :items="desserts" class="elevation-1">
      <template v-slot:item.actions="{ item }">
        <v-btn color="green"  @click="checkReport(item)">查看报告</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  created(){
    // created每次刷新页面都会调用的方法
    this.getTaskList()
  },
  methods: {
    // 获取task数据信息
    getTaskList(){

      // console.log(this.$api.task)
      // 调用task 的get接口，从接口获取数据库的task数据信息
      this.$api.task.getTask().then((result) => {
      // // 拿到结果信息后，赋值给dessert 做前端展示
        // console.log(result)
        this.desserts = result.data.msg.data
      })
    },
    checkReport(item){
      // 打开报告链接
      window.open(item.report)
    }


  },
  data() {
    return {
      headers: [
        {
          text: "任务ID",
          align: "start",
          sortable: false,
          value: "id"
        },
        { text: "任务描述", value: "remark" },
        { text: "创建时间", value: "create_at", sortable: true },
        { text: "Actions", value: "actions"}

      ],
      desserts: []
    };
  }
};
</script>