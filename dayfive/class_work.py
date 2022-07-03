# 1、将字符串类似："k:1|k3:2|k2:9" 处理成key:value,比如{"k": "1", "k3": "2"}



# 2、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 并最终通过#get(key)的方式取出对应的value值。
# url地址如下：
url = "http://ip:port/extername/get_account_trade_record.json?#page_size=20&page_index=1&user_id=203317&trade_type=0"


index_wen = url.index("?")
url = url[index_wen+1:]
url = url.replace("#", "")
url_list = url.split("&")
result_dict = {}
for i in url_list:
    kv_list = i.split("=")
    result_dict[kv_list[0]] = kv_list[1]
result = result_dict.values()
a = 0

