# _*_coding:utf-8 _*_
# @Time     : 2024/7/21 10:58
# @Author   : anliu
# @File     : test_file_path.py
# @Theme    : PyCharm

import os
import sys

# 获取当前脚本的绝对路径
script_path = os.path.abspath(__file__) # __file__是一个内置变量，表示当前文件的路径
print('abspath\t', script_path)

# 获取当前脚本的绝对路径
script_path = os.path.abspath('.') # __file__是一个内置变量，表示当前文件的路径
print('abspath .\t', script_path)

# 获取当前工作目录
current_working_directory = os.getcwd()
print('getcwd\t', current_working_directory)