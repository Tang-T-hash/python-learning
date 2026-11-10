# #先定义，后调用   只有调用才会执行
# def out_line():
#     print("-----------------")
#     print("-----------------")
#
# #调用
# out_line()
# out_line()
# out_line()
from audioop import avg


#函数的参数和返回值

# #计算圆的面积
# def circle_area(r):
#     return 3.14 * r * r
#
# circle = circle_area(5)
# print(circle)
#
# print("-----------------------------")
# #计算长方形的面积
# def rectangle_area(l, w):
#     return l * w
#
# rectangle = rectangle_area(5, 5)
# print(rectangle)
#
# print("-----------------------------")
#
# #返回多个值
# # def circle_area_len(r):
# #     return 3.14 * r * r, 2 * 3.14 * r
# #
# # circle = circle_area_len(5)
# # print(circle)
#
# #取一位小数   round()
# def circle_area_len(r):
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r:   半径
#     :return:   圆的面积    圆的周长
#     """
#     return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
#
# circle = circle_area_len(5)
# print(circle)


# d = int(input("请输入底长："))
# h = int(input("请输入高："))
# def triangle_area(d, h):
#     """
#     根据传入的底和高计算三角形的面积
#     :param d:  底
#     :param h:  高
#     :return: 三角形面积
#     """
#     return d * h / 2
# san = triangle_area(d, h)
# print(f"底为{d}, 高为{h},面积为：{san}")



#定义一个函数：计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)
#
# def count_aeiou(s):
#     """
#         计算字符串中元音字母的个数
#     :param s: 字符串
#     :return:  元音字母的个数
#     """
#     num = 0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num += 1
#
#     return num
# print(count_aeiou("FHELLO houulae ok"))


# def calc_score(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分，最低分， 平均分
#     :param score_list: 分数列表
#     :return:   最高分， 最低分， 平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg_s
#
# s_list = [456, 645, 454, 666, 545, 573, 674,700]
# max_score, min_score, avg_score = calc_score(s_list)
# print("最高分：", max_score)
# print("最低分：", min_score)
# print("平均分：", avg_score)



#全局变量
num = 100

def circle_area(R):
    #局部变量
    pi = 3.14
    area = pi * R * R
    # global关键字用于明确告诉python解释器  在函数中要使用全局变量，使得可以在函数内部修改全局变量的值
    global num
    num = 10000
    print("num=",num)

    return area

#调用函数
c_area = circle_area(10)
print(c_area)

print("num=", num)
