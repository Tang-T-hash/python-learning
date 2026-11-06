# #key不能重复（如果重复，后面的值会覆盖前面的值）
# dict1 = {"小白":670, "小黑":650, "小红":569, "小灰":500}
# print(dict1)
# print(type(dict1))
#
# #key必须得是不可变类型(str, int, float, tuple)  不能是  List  set  dict
# dict2 = {1:599, 2:498, 3.6:600, (1,2):700}
# print(dict2)
#
# #访问
# print(dict1["小白"])   #获取
# dict1["小黑"] = 560    #修改
# print(dict1)
#
# print("------------------------------------")
#
# dict1["涛哥"] = 400   #添加   key不存在就是添加
# print(dict1)
#
# dict1["小灰"] = 720    #key存在就是修改
# print(dict1)
#
# print(dict1["小白"])  #根据key获取value
# print(dict1.get("涛哥"))
# print(dict1.keys())    #获取所有的key
# print(dict1.values())   #获取所有的value
# print(dict1.items())    #获取所有的键值对  key:value
#
# print("--------------------------------")
# #删除
# score = dict1.pop("小红")
# print(score)  #拿到删除的值
# print(dict1)
#
# del dict1["小黑"]
# print(dict1)
#
#
# print("------------------------------------")
# #遍历
# #法一
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# print("------------------------------------")
# #法二
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
#
# print("------------------------------------")
# #法三
# for k, v in dict1.items():
#     print(f"{k}: {v}")
#




"""
    案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车

    结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""

# shopping_cart = {}
#
# menu = """
# #################购物车系统#####################
# #               1.添加购物车                  #
# #               2.修改购物车                  #
# #               3.删除购物车                  #
# #               4.查询购物车                  #
# #               5.退出购物车                  #
# ##############################################
# """
# print("欢迎使用购物车管理系统！")
#
# while True:
#     print(menu)
#
#     choice = input("请选择要执行的操作(1-5)")
#
#     match choice:
#         case "1":
#             goods_name = input("请输入商品的名称")
#             goods_price = float(input("请输入商品的价格"))
#             goods_num = int(input("请输入商品的数量"))
#
#             if goods_name in shopping_cart:
#                 print("商品已存在，请重新选择！！")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("商品添加完毕！！")
#         case "2":
#             goods_name = input("请输入要修改商品的名称")
#             if goods_name not in shopping_cart:
#                 print("商品不存在，请重新选择！！")
#                 continue
#
#             goods_price = float(input("请输入商品最新的价格"))
#             goods_num = int(input("请输入商品最新的数量"))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕！！")
#         case "3":
#             goods_name = input("请输入要删除商品的名称")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，删除失败")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕")
#         case "4":
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量{goods_info['num']}")
#         case "5":
#             print("拜拜")
#             break
#         case _:
#             print("非法操作，不支持！！！")



#案例练习  结构: study_cart = {"小黑": {"chinese": 99, "math": 82, "english":90}, "小白": {...}}

study_cart = {}

menu = """
##################教务管理系统##################
#                 1.添加学生信息                #
#                 2.修改学生信息                #
#                 3.删除学生信息                #
#                 4.查询学生信息                #
#                 5.列出所有学生                #
#                 6.统计班级成绩                #
#                 7.退出系统                    #
###############################################
"""

print("欢迎使用教务管理系统")
while True:
    print(menu)

    choice = input("请选择你要进行的操作(1-7)")
    match choice:
        case "1":
            name = input("请输入你的姓名")
            chinese = int(input("请输入你的语文成绩"))
            math = int(input("请输入你的数学成绩"))
            english = int(input("请输入你的英语成绩"))

            if name in study_cart:
                print("学生信息已存在，请重新添加！！")
            else:
                study_cart[name] = {"chinese": chinese, "math": math, "english": english}
                print("学生信息添加完毕！！")
        case "2":
            name = input("请输入你的姓名")
            if name not in study_cart:
                print("学生信息不存在，请重新输入")
                continue
            chinese = int(input("请输入你的语文成绩"))
            math = int(input("请输入你的数学成绩"))
            english = int(input("请输入你的英语成绩"))
            study_cart[name] = {"chinese": chinese, "math": math, "english": english}
            print("学生信息修改成功")
        case "3":
            name = input("请输入你的姓名")
            if name not in study_cart:
                print("删除失败，学生信息不存在，请重新输入")
            else:
                del study_cart[name]
                print("删除成功")
        case "4":
            name = input("请输入你要查询的学生姓名")
            if name not in study_cart:
                print("查询失败，该学生信息不存在")
            else:
                info = study_cart[name]
                print(f"姓名：{name}, 语文成绩：{info['chinese']}, 数学成绩：{info['math']}, 英语成绩：{info['english']}")
        case "5":
            for name in study_cart.keys():
                info = study_cart[name]
                print(f"姓名：{name},语文成绩：{info['chinese']},数学成绩{info['math']},英语成绩{info['english']}")
        case "6":
            if not study_cart:
                print("还没有学生信息，请先添加")
                continue

            subjects = {"chinese": "语文", "math": "数学", "english": "英语"}
            print("========== 班级成绩统计 ==========")
            for key, label in subjects.items():
                # 取出这一科所有学生的成绩
                scores = [info[key] for info in study_cart.values()]
                max_score = max(scores)
                min_score = min(scores)
                avg_score = sum(scores) / len(scores)

                # 最高/最低可能并列，把所有名字都找出来
                max_names = "、".join([name for name, info in study_cart.items() if info[key] == max_score])
                min_names = "、".join([name for name, info in study_cart.items() if info[key] == min_score])

                print(f"{label} 最高分：{max_score}（{max_names}），最低分：{min_score}（{min_names}），平均分：{avg_score:.1f}")
            print("==================================")
        case "7":
            break
        case _:
            print("非法操作")

