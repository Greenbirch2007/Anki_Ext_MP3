
from Two_dict import base_dict
import os
import xlrd
import sys


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")




if __name__ == '__main__':
    lpath =  "/root/d"
    path0 = lpath
    path1 = lpath
    excelFile = '{0}/list_d.xlsx'.format(lpath)
    full_items = read_xlrd(excelFile=excelFile)
    getdict = dict(full_items)
    print(base_dict)
    print(getdict)

    for k1,v1 in base_dict.items():
        for k2,v2 in getdict.items():
            if v1==v2:
                # print((k1,k2))

                sys.path.append(path1)
                # print(sys.path)
                # 列出当前目录下所有的文件
                files = os.listdir(path0)
                # files = os.listdir('.')
                # print('files', files)
                for filename in files:
                    # 用于看后缀
                    portion = os.path.splitext(filename)
                    first_name= k1
                    last_name= k2


                    if portion[1] == "" and portion[0]==first_name:
                        #         # 重新组合文件名和后缀名
                        newname = last_name + ".mp3"
                        os.rename(filename,newname)
                    #

