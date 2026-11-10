# def reg_stu(name, age, gender, city):
#     print(f"注册成功：姓名：{name}, 年龄：{age}, 性别：{gender}, 城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# #位置参数
# stu = reg_stu("张三", 18, "男", "北京" )
# print(stu)
# print("-----------------------------------")
# #关键字参数
# stu = reg_stu(name = "王林", age = 28, gender = "男", city = "广东" )
# print(stu)
# #换位置也不影响
# stu = reg_stu( gender = "男", age = 28, city = "广东", name = "王林" )
# print(stu)
# print("-----------------------------------")
#
#  #位置参数 + 关键字参数   位置参数在前  关键字参数在后
# stu = reg_stu("李四", "男", gender=28, city = "广东",  )
# print(stu)


# #默认参数要写在非默认参数后面
# def reg_stu(name, age, gender = "男", city = "北京"):
#     print(f"注册成功：姓名：{name}, 年龄：{age}, 性别：{gender}, 城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# #调用
# stu = reg_stu("王林", 20)
# print(stu)
#
# stu = reg_stu("李慕婉", 19, "女", "湖南")
# print(stu)
#
# stu = reg_stu("韩立", 22, city = "上海")
# print(stu)

#------------------------------ 函数  不定长参数(位置参数  *args  元组  --------------------------------

#根据传入的这些数据，计算这批数据的最小值  最大值，平均值

# def calc_data(*args):
#     max_data = max(args)
#     min_data = min(args)
#     avg_data = sum(args)/len(args)
#     return max_data, min_data, round(avg_data, 1)
#
# #调用
# print(calc_data(2, 7, 9, 10, 45))
#
# print(calc_data(2, 7, 9, 10, 45, 90, 94, 100, 222))



#------------------------------ 函数  不定长参数(关键字参数  **kwargs  字典  --------------------------------

# def calc_data(*args, **kwargs):
#     """
#         根据传入的这些数据，计算这批数据的最小值  最大值，平均值
#     :param args:  不定长位置参数
#     :param kwargs:  不定长关键字参数
#        round: 保留小数位个数
#        print: 是否打印输出
#     :return:  最小值，最大值，平均值
#
#     """
#     max_data = max(args)
#     min_data = min(args)
#     avg_data = sum(args)/len(args)
#
#     if kwargs.get('round') is not None:
#         avg_data = round(avg_data, kwargs.get('round'))
#
#     if kwargs.get('print'):
#         print(f"计算出来的最大值：{max_data}, 最小值：{min_data}, 平均值：{avg_data}")
#
#     return max_data, min_data, avg_data
#
# #调用
# print(calc_data(2, 7, 9, 10, 45, 673, round = 2, print = True))

# print(calc_data(2, 7, 9, 10, 45, 90, 94, 100, 222))


print("--------------------------------------------------------------")

#函数的参数类型
#加
def add(x, y):
    return x + y
#减
def subtract(x, y):
    return x - y
#乘
def multiply(x, y):
    return x * y
#除
def divide(x, y):
    return x / y

#计算
def calc(x, y, oper):
    return oper(x, y)

# print(calc(10, 20, add))  #加
# print(calc(10, 20, subtract))   #减
# print(calc(10, 20, multiply))  乘
print(calc(10, 20, divide))   #除