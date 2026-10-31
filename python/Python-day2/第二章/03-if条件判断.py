# score = int(input("请输入你的分数："))
# if score >= 680:
#     print("欢迎来清华")
#     print("欢迎来北大")
#
# print("-----------")


# ok_account = "1888888"
# ok_password = "666888"
#
# account = input("请输入你的账号：")
# password = input("请输入你的密码：")
#
# if account == ok_account and password == ok_password:
#     print("登陆成功")
#     print("进入b站首页")
#
# if account != ok_account or password != ok_password:
#         print("登陆失败")
#         print("账号或密码错误")


# ok_account = "1888888"
# ok_password = "666888"
#
# account = input("请输入你的账号：")
# password = input("请输入你的密码：")
#
# if account == ok_account and password == ok_password:
#     print("登陆成功")
#     print("进入b站首页")
#
# else:
#         print("登陆失败")
#         print("账号或密码错误")



# year = int(input("请输入要判定的年份："))
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")


# a = int(input("请输入一个数："))
# if a > 0:
#     print(f"{a}是正数")
# elif a < 0:
#     print(f"{a}是负数")
# else:
#     print("0")


"""
account = input("请输入账号：")
password = input("请输入密码：")
if (account == "admin" and password == "666888"):
    print("登陆成功")
elif account == "root" and password == "547527":
    print("登录成功")
elif account == "zhangsan" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败,账号或密码错误")
"""



a = int(input("请输入第一条边长"))
b = int(input("请输入第二条边长"))
c = int(input("请输入第三条边长"))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("这是一个等边三角形")
    elif  a == b or b == c or a == c:
        print("这是一个等腰三角形")
    else:
        print("这是一个普通三角形")
else:
    print(f"{a}{b}{c} 这三个边长不能构成三角形！！！")
