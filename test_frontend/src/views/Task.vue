<template>
  <div>
    <v-data-table :headers="headers" :items="desserts" class="elevation-1">
      <template v-slot:item.actions="{ item }">
        <v-btn color="green"  @click="editItem(item)">查看报告</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
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
        { text: "Actions", value: "actions", sortable: false }

      ],
      desserts: [
        {
          id: "任务1",
          remark: 452
        },
        {
          id: "任务2",
          remark: 452
        }
      ]
    };
  }
};
</script>