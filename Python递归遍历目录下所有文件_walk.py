# coding:utf-8
# os.walk(top)
# 遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])

import os
path=r'C:\Users\Administrator\Desktop\os_test'
# path=r'D:\desktop'
file_path_list=[]
file_name_list=[]
for fpathe,dirs,fs in os.walk(path):
    for f in fs:
        file_path_list.append(os.path.join(fpathe,f))
        file_name_list.append(f)
print(file_path_list)
# print(file_path_list.index([]))
# print(file_name_list.index([]))