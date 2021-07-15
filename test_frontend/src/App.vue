<template>
  <div id="app">
    <!-- App.vue -->
    <v-app>
      <v-navigation-drawer app>
        <!-- -->
      </v-navigation-drawer>

      <v-app-bar app>
        <!-- -->
      </v-app-bar>

      <!-- 根据应用组件来调整你的内容 -->
      <v-main>
            <router-view></router-view>


        <!-- 给应用提供合适的间距 -->
        <v-container fluid>

          <!-- 如果使用 vue-router -->
          <router-view></router-view>
        </v-container>
      </v-main>

      <v-footer app>
        <!-- -->
      </v-footer>
    </v-app>
    <!-- 渲染路由对应的页面 -->
    <!-- <router-view> -->
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
