#导入模块 import ... ---> 调用方式： 模块名.功能名/别名.功能名
# import random
# import random as rd
# for i in range(100):
#     # print(random.randint(1, 100))
#     print(rd.randint(1, 100))
from random import randint

#2.导入模块中的功能   from ... import ....  ----> 调用方式：功能名 / 别名
# # from random import randint
# from random import randint as rint
# for i in range(100):
#     # print(randint(1, 100))
#     print(rint(1, 100))


from random import *    #一般写在整个文件最上面
for i in range(100):
    print(randint(1, 100))
