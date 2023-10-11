# coding:utf-8
# 自定义函数
import os
path=r'D:\desktop'
if os.path.exists(path):
    print(path,'存在')
else:
    print(path,'不存在')
    
def gci(path):
    file_path_list=[]
    # 获取path文件下内的所有文件夹及文件 名称
    parents=os.listdir(path)
    for parent in parents:
        child=os.path.join(path,parent)
        # child可能是文件夹名称,如果是文件夹则继续深入查找文件
        if os.path.isdir(child):
            gci(child)
        else:
            file_path_list.append(child)
            # child是一个列表
            # print(child)
    print(file_path_list)
    # print(file_list.index([]))
if __name__=='__main__':
    gci(path)