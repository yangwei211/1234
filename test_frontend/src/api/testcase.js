import axios from "./http"

// 属于testcase 的一些接口信息
const testcase = {
    // 获取用例信息
    getTestcase(){
        return axios({
            method: 'get',
            url: '/testcase',
          })
    },
    // 删除接口需要传递id进行删除
    deleteTestcase(params){
        return axios({
            method: 'delete',
            url: '/testcase',
            // 传url参数使用params
            params: {id: params}
        })
        
    },
    updateTestcase(params){
        return axios({
            method: 'put', 
            url: '/testcase',
            // 使用data参数传递请求体
            data: params
        })

    },
    // 2. 完成添加接口数据
    addTestcase(params){
        return axios({
            method: 'post', 
            url: '/testcase',
            // 使用data参数传递请求体
            data: params
        })
    }
}

export default testcase