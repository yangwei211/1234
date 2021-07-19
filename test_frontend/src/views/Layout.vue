<template>
  <!-- App.vue -->
  <v-app>
    <v-navigation-drawer app>
      <!-- 抽屉导航放在这里 -->
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-h6">测试平台</v-list-item-title>
              <v-list-item-subtitle>ad</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list dense nav>
            <v-list-item v-for="item in items" :key="item.title" link
            @click="switchTab(item)"
            >
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
    </v-navigation-drawer>
    <v-app-bar app>
    </v-app-bar>
    <!-- 根据应用组件来调整你的内容 -->
    <v-main>
      <!-- 根据路由展示对应的组件 -->
      <router-view></router-view>
    </v-main>
    <v-footer app>
    </v-footer>
  </v-app>
  <!-- 渲染路由对应的页面 -->
  <!-- <router-view> -->
</template>


<script>
  export default {
    data () {
      return {
        items: [
          { title: '测试用例', icon: 'mdi-view-dashboard', router: "testcase"},
          { title: '测试任务', icon: 'mdi-image', router: "task"},
        ],
        right: null,
      }
    },
    methods: {
        switchTab(item){
            // 传入切换路由的名称，就会切换到对应的路由地址
            this.$router.push({name: item.router})
        }
    }

  }
</script>