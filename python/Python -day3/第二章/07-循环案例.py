for i in range(1, 6):
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")
    if username == "" or password == "":
        print("不能为空")
        continue

    if username == "admin" and password == "666888":
        print("登陆成功")
        break
    elif username == "root" and password == "123456":
        print("登录成功")
        break
    elif username == "zhangsan" and password == "888666":
        print("登录成功")
        break
    else:
        if i < 5:
            print(f"错误，还剩{5 - i}次机会")
else:
    print("次数用尽")


