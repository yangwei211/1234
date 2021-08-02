// 测试任务接口管理
import axios from "./http"

// 属于testcase 的一些接口信息
const task = {
    // 获取用例信息
    getTask(){
        return axios({
            method: 'get',
            url: '/task',
          })
    },

    // 2. 完成添加一条任务记录，并且执行用例
    addTask(params){
        return axios({
            method: 'post', 
            url: '/task',
            // 使用data参数传递请求体
            data: params
        })
    }
}

export default task