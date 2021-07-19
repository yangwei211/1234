// axios的引用
import axios from 'axios'

var instance = axios.create({
    // 配置了每个请求的头信息
    headers: {
        'Content-Type':'application/json'
    },
    // 配置了baseurl，基础的地址存放了 http协议、 域名、端口等信息
    
    baseURL:'http://127.0.0.1:5000/'
})

// 如果要给别的地方使用，还需要加一个export default
export default instance