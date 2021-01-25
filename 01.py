# coding:utf-8
'''
import requests,json
def GetToken():
    token_url = 'http://47.96.181.17:9090/rest/toController'
    payload = {"userName":"J201903070064","password":"362387359"}
    token_header = {'Content-Type':'application/json'}
    #获取token值：使用账号密码去验证，获取这个值
    reqs=requests.post(token_url,json=payload)#发送post请求到url
    # post方法的参数有：“url,data=None,json=None,**kwargs”
        # 如果body体选择json，则默认头部信息就是application/json，header就可以省略,不省略就得这样写：reqs=requests.post(token_url,json=payload,headers=token_header)。
        # 如果body体选择data，则默认头部信息就是表单格式
    #打印响应数据
    #方案一：输出是字符串格式
    #print(reqs.text)
    #print(json.loads(reqs.text))#json.loads()可以把子字符串转换为字典;json.dumps()可以把字典转换为字符串
    #方案二：输出是字典格式
    return reqs.json()['token']

token = GetToken()
print(token)
user_url='http://47.96.181.17:9090/rest/ac01CrmController'
payload={"aac003": "张三", "aac004": "1", "aac011": "21", "aac030": "13575726577", "aac01u": "88002255", "crm003": "1", "crm004": "1", "crm00a": "2018-11-11", "crm00b": "aaaaaa", "crm00c": "2019-02-28", "crm00d": "bbbbbb"}
user_header={'X-AUTH-TOKEN':token}
reqs=requests.post(user_url,json=payload,headers=user_header)
data = reqs.json()
print(data)
'''
'''
import xlrd
from xlutils.copy import copy
#xlrd 2.0.1版本只支持.xls文件，如果要使用xlsx文件可以回退到低版本先卸载pip uninstall xlrd再安装pip install xlrd==1.2.0
dir='.\接口测试测试用例模板.xls'
data=xlrd.open_workbook(dir,formatting_info=True)
sheet1=data.sheet_by_name('新增客户')
#print(sheet1.cell(1,5).value)
newworkbook=copy(data)
dir1='.\\result'
newworkbook.save(dir1)
'''
'''
for i in range(1,3):
    print(i)
'''
'''
num = 10
for i in range(0,num):
    print('  ',end = '')
    print("*",end= ' ')
print()
for x in range(0,num):
    for y in range(-num,num):
        if abs(x)+abs(y) <= num -2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
'''
'''
num = input()
for i in range(0,num):
    print('  ',end = '')
    print("*",end= ' ')
print()
for x in range(0,num):
    for y in range(-num,num):
        if abs(x)+abs(y) <= num -2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
'''
'''
x=int(input())
for i in reversed(range(1,x+1)):
    print(' '*(x-i),end='')
    print('* '*i,end='')
    print(' '*(x-i))
'''
'''
li=[1,3,4,6,4,7,8,1]
li.sort()
n=li[-1]
for i in range(len(li)-2,-1,-1):
    if n == li[i]:
        li.remove(li[i])
    else:
        n = li[i]
print(len(li))
'''
import requests,xlrd,xlutils.copy,ast,pytest

file1 = '.\接口测试测试用例模板.xls'
data = xlrd.open_workbook(file1, formatting_info=True)  # 打开原始文件
indata = data.sheet_by_name('用户登录')  # 获取"用户登录"这个标签页
rows = indata.nrows  # 获取行数
cols = indata.ncols  # 获取列数
CellIndata=[indata.cell_value(i, 5) for i in range(1, rows)]
print(CellIndata)