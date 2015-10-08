#下面两种方式都都可以用于引入一个模块
#第一种用法在使用模块内部的类型时候需要继续sys.xxx调用
#第二种用法是直接将名字导入到局部命名空间中了，在使用的时候直接使用即可。
import sys
from os import path
print("The Python Path is",sys.path, "\n")
print("file size ", path.getsize("/home/tnqiangren/hello"))
