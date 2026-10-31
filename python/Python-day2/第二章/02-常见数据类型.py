#字符串
s1 = "hello"  #双引号定义
s2 = 'world'  #单引号定义

s3 = """
hello:
      欢迎大家
      大家记得
"""   # 三引号定义（多行字符串 ）
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))

s4 = 'It\'s very interesting'
print(s4)
s5 = "hello 的意思是\"你好\""
print(s5)
s6 = 'hello 的意思是\"你好\"'
print(s6)

print('\t欢迎大家加入python大家庭！\n\t记得点赞')   #\n  换行  \t 按了tab缩进


#案例
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "python, java"
print("大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro + "，爱好是" + hobby)
#   %s 占位符
print("大家好，我是%s，今年%s岁，学习的专业是%s，爱好是%s" % (name,age,pro,hobby))
#    f"..{变量名/表达式} .."                                                  推荐写法
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{pro}，爱好是{hobby}")



# input()
# name = input("请输入名字")
# age = input("请输入年龄")
# print(f"你的姓名是：{name}，年龄是：{age}")


#案例  银行卡ATM取款
# 总金额
# total = 10000
# #1.输密码
# mi = input("请输入你的密码")
# print(f"密码正确:{mi}")
#
# #2.输入取款金额
# qu = input("请输入取款金额:")
#
# #3.计算余额并输出
# print(f"你的余额为：{total},取款后金额为：{total - int(qu)}")


# a = input("请输入第一个数字")
# b = input("请输入第二个数字")
# print(f"两个数的和为：{int(a) + int(b)}")

# x = float(input("请输入第一个数字"))
# y= float(input("请输入第二个数字"))
# print("两个数的和为：", x + y)
# print("两个数的差为：", x - y)


# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# c = int(input("请输入第三个数："))
# print("平均数：", (a+b+c) / 3)

# a = int(input("请输入梯形的上底"))
# b = int(input("请输入梯形的下底"))
# c = int(input("请输入梯形的高"))
# print("梯形的面积是：", (a + b) * c / 2)


# a = int(input("请输入体重（单位/kg）"))
# b = int(input("请输入身高(单位/m)"))
# print("身体质量指数BMI为：", a / (b ** 2))

# a = int(input("请输入一个值"))
# print(f"{a}在10-20之间：", a >= 10 and a <= 20)

a = int(input("请输入一个值"))
print(f"{a}不在10-20之间：", a <= 10 or a >= 20)
