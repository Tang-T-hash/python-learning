# day = input("请输入星期几（1-7）")

# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6" | "7":
#         print("周末")
#     case _:
#         print("输入有误！！！")



# 简易计算器
# num1 = int(input("请输入第一个数"))
# num2 = int(input("请输入第二个数"))
# c = input("请输入运算符号（+ - * /）")
# match c:
#     case "+":
#         print(f"两数之和为：{num1 + num2}")
#     case "-":
#         print(f"两数之差为：{num1 - num2}")
#     case "*":
#         print(f"两数之积为：{num1 * num2}")
#     case "/" if num2 != 0:   #if条件成立才匹配这个case
#         print(f"两数之除为：{num1 / num2}")
#     case _:
#         print("输入运算方法有误")




num = input("请玩家输入你的动作（上/W/w, 下/S/s, 左/A/a， 右/D/d, 跳/""(空格), 攻击/J/j, 退出/ESC/esc）")
match num:
    case "上" | "W" | "w":
        print("角色向上移动")
    case "下" | "S" | "s":
        print("角色向下移动")
    case "左" | "A" | "a":
        print("角色向左移动")
    case "右" | "D" | "d":
        print("角色向右移动")
    case "跳" | " "" ":
        print("角色跳跃")
    case "攻击" | "J" | "j":
        print("角色发动攻击")
    case "退出" | "ESC" | "esc":
        print("角色退出游戏")
    case _:
        print("输入有误")