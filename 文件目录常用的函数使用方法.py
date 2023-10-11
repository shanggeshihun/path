 # os、os.path 模块中关于文件、目录常用的函数使用方法 
"""
os模块中关于文件/目录常用的函数使用方法

getcwd()
返回当前工作目录

chdir(path)
改变工作目录

listdir(path='.')
列举指定目录中的文件名及文件夹名（'.'表示当前目录，'..'表示上一级目录,目录下无文件或文件夹则为空）

mkdir(path)
创建单层目录，如该目录已存在抛出异常

makedirs(path)
递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突

remove(path)
删除文件

rmdir(path)
删除单层目录，如该目录非空则抛出异常

removedirs(path)
递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常

rename(old, new)
将文件old重命名为new

system(command)
运行系统的shell命令

walk(top)
遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])【具体实现方案请看：第30讲课后作业^_^】
以下是支持路径操作中常用到的一些定义，支持所有平台

os.curdir
指代当前目录（'.'）

os.pardir
指代上一级目录（'..'）

os.sep
输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）

os.linesep
当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）

os.name
指代当前使用的操作系统（包括：'posix',  'nt', 'mac', 'os2', 'ce', 'java'）
"""

# os.path模块中关于路径常用的函数使用方法
"""
basename(path)
去掉目录路径，单独返回文件名或者文件夹名

dirname(path)
去掉文件名，单独返回目录路径

join(path1[, path2[, ...]])
将path1, path2各部分组合成一个路径名

split(path)
分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在

splitext(path)
分离文件名与扩展名，返回(f_name, f_extension)元组

getsize(file)
返回指定文件的尺寸，单位是字节

getatime(file)
返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

getctime(file)
返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

getmtime(file)
返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
以下为函数返回 True 或 False

exists(path)
判断指定路径（目录或文件）是否存在

isabs(path)
判断指定路径是否为绝对路径

isdir(path)
判断指定路径是否存在且是一个目录

isfile(path)
判断指定路径是否存在且是一个文件


islink(path)
判断指定路径是否存在且是一个符号链接

ismount(path)
判断指定路径是否存在且是一个挂载点

samefile(path1, paht2)
判断path1和path2两个路径是否指向同一个文件
"""

# E:\NOTEPAD\NOTE\Python\文件目录常用的函数使用方法.py
import os 

# print('当前工作目录',os.getcwd());

# print('. 指定目录下当前目录下的文件夹名及文件名',os.listdir(r'c:\users\administrator\desktop\os_test\.'))
# print('. 指定目录下上级目录下的文件夹名及文件名',os.listdir(r'c:\users\administrator\desktop\os_test\..'))
# print(os.listdir(r'C:\Users\Administrator\Desktop\os_test\os_test_son_2\os_test_son2_son'))


# print('. 指定目录下创建文件名os_test_son_1',os.mkdir(r'c:\users\administrator\desktop\os_test\os_test_son_1'))

# print('. 指定目录下创建文件名os_test_son_2及子文件夹os_test_son2_son',os.makedirs(r'c:\users\administrator\desktop\os_test\os_test_son_2\os_test_son2_son'))

# print('. 删除文件test1.txt',os.remove(r'c:\users\administrator\desktop\os_test\test1.txt'))

# os_test_son目录下有文件test2.txt  故报错
# print('. 删除单层目录os_test_son',os.rmdir(r'c:\users\administrator\desktop\os_test\os_test_son'))

# print('. 删除单层目录os_test_son',os.rmdir(r'c:\users\administrator\desktop\os_test\os_test_son_1'))

# C:\Users\Administrator\Desktop\os_test\os_test_son_3\os_test_son_2_son
# 遇到目录非空则抛出异常
# print('. 删除os_test_son_3及其子目录',os.removedirs(r'C:\Users\Administrator\Desktop\os_test\os_test_son_3'))

w=os.walk(r'C:\Users\Administrator\Desktop\os_test')
w_lst=[f for f in w]
print(w_lst) 


import os.path 

# print('返回当前文件夹名或者文件名',os.path.basename(r"C:\Users\Administrator\Desktop\os_test\os_test_son\test2.txt"))

# print('去掉文件名或文件夹名单独返回目录路径',os.path.dirname(r"C:\Users\Administrator\Desktop\os_test\os_test_son\test2.txt"))
# print('去掉文件名或文件夹名单独返回目录路径',os.path.dirname(r"C:\Users\Administrator\Desktop\os_test\os_test_son"))

# print('分割文件名与路径',os.path.split(r"C:\Users\Administrator\Desktop\os_test\os_test_son\test2.txt"))
# print('分割文件夹名与路径',os.path.split(r"C:\Users\Administrator\Desktop\os_test\os_test_son"))


# print('分离文件名与扩展名',os.path.splitext(r"C:\Users\Administrator\Desktop\os_test\os_test_son\test2.txt"))
# print('分离文件名与扩展名,如果没有文件则元组第二个元素为空',os.path.splitext(r"C:\Users\Administrator\Desktop\os_test\os_test_son"))

# print('判断指定路径（目录或文件）是否存在',os.path.exists(r"C:\Users\Administrator\Desktop\os_test\os_test_son"))

# print('判断指定路径是否存在且是一个目录',os.path.isdir(r"C:\Users\Administrator\Desktop\os_test\os_test_son"))#true
# print('判断指定路径是否存在且是一个目录',os.path.isdir(r"C:\Users\Administrator\Desktop\os_test\os_test_son\test2.txt"))#false

# print('判断指定路径是否存在且是一个文件',os.path.isfile(r"C:\Users\Administrator\Desktop\os_test\os_test_son\test2.txt"))#true
# print('判断指定路径是否存在且是一个文件',os.path.isfile(r"C:\Users\Administrator\Desktop\os_test\os_test_son"))#false

# print('最后”/”开头的的开始往后拼接，之前的参数全部丢弃。',os.path.join(r'c:\users\administrator\desktop\os_test','\os_test_son'))#返回os_test_son
# print('最后”/”开头的的开始往后拼接，之前的参数全部丢弃。',os.path.join(r'c:\users\administrator\desktop\os_test','os_test_son'))#返回c:\users\administrator\desktop\os_test\os_test_son
# print('最后”/”开头的的开始往后拼接，之前的参数全部丢弃。',os.path.join(r'c:\users\administrator\desktop\os_test','os_test_son','test2.txt'))#返回c:\users\administrator\desktop\os_test\os_test_son\test2.txt'

# print(os.path.join('a','b','c')) #返回a\b\c


