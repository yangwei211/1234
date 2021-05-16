import json


def recursion(data):
    """
    :param data: 原始的数据
    :return: 在原始数据基础之上，修改float 类型，对float 类型做数据翻倍操作
    """
    #
    if isinstance(data, dict):
        # 如果是字典类型，继续递归value值
        for k, v in data.items():
            data[k] = recursion(v)
    elif isinstance(data, list):
        # 递归算法，如果是list 就继续遍历列表中的元素
        # data_new = []
        # for item in data:
        #     data_new.append(handle_data(item))
        # data_new = []
        # for i in data:
        #     data_new.append(recursion(i))
        #
        data = [recursion(i) for i in data]
    elif isinstance(data, float):
        # 对浮点型做倍增
        data = data*2
    else:
        data = data

    return data

if __name__ == '__main__':
    test_data = json.load(open("quote.json", encoding="utf-8"))
    print(json.dumps(recursion(test_data), indent=2))



