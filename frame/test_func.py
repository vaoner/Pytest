# coding:utf-8
'''
import pytest
#@pytest.mark.parametrize('a',[1,2])#数据驱动，即参数化，这里将1和2传入test函数，做两次对比
@pytest.mark.parametrize('a,b',[(4,3),(3,4)])#这里表示a取1b取2，相加和7对比，然后a取3b取4相加再和7对比
#def test_001(a):
def test_001(a,b):
    print('----开始----')
    #assert a == 1
    assert a+b == 7
    print('----结束----')
#def test_002():
#    assert 1+3 == 4
#class Test_login(object):
#    def test_003(self):
#        assert 1+5 == 4

if __name__ == '__main__':#在 if __name__ == 'main': 下的代码只有在py文件作为脚本直接执行时才会被执行，而 import 到其他脚本中是不会被执行的
    pytest.main(['test_func.py'],'-s')#加-s表示打印函数中的print内容，默认不打印
'''
import requests,xlrd,xlutils.copy,ast,pytest

file1 = '.\接口测试测试用例模板.xls'
data = xlrd.open_workbook(file1, formatting_info=True)  # 打开原始文件
indata = data.sheet_by_name('用户登录')  # 获取"用户登录"这个标签页
rows = indata.nrows  # 获取行数
cols = indata.ncols  # 获取列数
CellIndata=[indata.cell_value(i, 5) for i in range(1, rows)]
#print(CellIndata)

@pytest.mark.parametrize('x',CellIndata)
def test_login(x):
    url='https://www.wanandroid.com/user/login'
    x=ast.literal_eval(x)
    payload=x
    print(payload)
    reqs=requests.post(url,data=payload)#发送登录请求
    reqs1=reqs.json()['errorCode']#取登录请求返回值的状态码
    assert reqs1 == 0

if __name__ == '__main__':
    pytest.main(['test.func.py'],'-s','--html=..\\result.html')
