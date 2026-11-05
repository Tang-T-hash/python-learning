# #字符串  不可变
# s = "hello world"
# print(s)
# print(s[4])
# print(s[-7])
#
# for i in s:
#     print(i)
#
# #切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
#
# print(s[6:11:1])
# print(s[6::1])
# print(s[6:])
#
# print("--------------")
#
#
# print(s[-1:-6:-1])
# print(s[::-1])



# str = "    hello-world-hello-python   "
# print(str)
# #查找索引位置
# s1 = str.find("-")
# print(s1)
#
# #统计字符串再指定字符串中出现的次数
# s2 = str.count('h')
# print(s2)
#
# #转大写
# s3 = str.upper()
# print(s3)
# #转小写
# s4 = str.lower()
# print(s4)
#
# #将字符串按照指定字符串切割
# s5 = str.split('-')
# print(s5)
#
# #去除字符串两边的空格
# s6 = str.strip()
# print(s6)




# #方法1
# mail = input("请输入邮箱：")
#
# if mail.count('@') == 1 and mail.count('.') >= 1:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")
#


# # 方法2  in 运算符  判断自串是否在字符串中，存在，返回true:否则返回false
# mail = input("请输入邮箱：")
#
# if mail.count('@') == 1 and "." in mail:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")



