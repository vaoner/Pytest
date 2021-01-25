# cnding:utf-8
import requests,xlrd,xlutils.copy
from test02 import login

def result():
    file1='.\接口测试测试用例模板.xls'
    file2='.\接口测试测试用例结果.xls'
    data=xlrd.open_workbook(file1,formatting_info=True)#打开原始文件
    #print(data.nsheets)#获取标签页个数
    indata = data.sheet_by_name('用户登录')  # 获取"用户登录"这个标签页
    rows=indata.nrows#获取行数
    cols=indata.ncols#获取列数
    newdata = xlutils.copy.copy(data)  # 复制文件
    for i in range(1,rows):
        CellIndata=indata.cell_value(i,5)#获取第2行第6列这个单元格的数据
        #print(type((login(indata1))))
        res=login(CellIndata)#调用test02.py的login函数，取其结果为res
        newdata_sheet=newdata.get_sheet(5)#打开第6个页签
        newdata_sheet.write(i,7,res)#在坐标为1，7的单元格写入test02.py的执行结果（坐标从0开始计数）
    newdata.save(file2)#保存文件
result()