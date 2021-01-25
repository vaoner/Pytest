# cnding:utf-8
import requests,xlrd,xlutils.copy,ast
def login(x):
    url='https://www.wanandroid.com/user/login'
    #payload={'username':'wsyzxql123','password':'wsyzxql123'}
    x=ast.literal_eval(x)#这里不用json.loads将字符串转为字典是因为json.load规定了，字符串里面的值必须个个都是双引号的，而本次传入的带有单引号，因此用ast模块替代
    payload=x
    reqs=requests.post(url,data=payload)#发送登录请求
    reqs1=reqs.json()['errorCode']#取登录请求返回值的状态码
    if reqs1 == 0:#如果返回值为0表示请求成功
        return f'用例pass,耗时{reqs.elapsed.total_seconds()}秒'
    else:
        return f'用例fail,耗时{reqs.elapsed.total_seconds()}秒'
