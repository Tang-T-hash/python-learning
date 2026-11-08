# #先定义，后调用   只有调用才会执行
# def out_line():
#     print("-----------------")
#     print("-----------------")
#
# #调用
# out_line()
# out_line()
# out_line()



#函数的参数和返回值

#计算圆的面积
def circle_area(r):
    return 3.14 * r * r

circle = circle_area(5)
print(circle)

print("-----------------------------")
#计算长方形的面积
def rectangle_area(l, w):
    return l * w

rectangle = rectangle_area(5, 5)
print(rectangle)

print("-----------------------------")

#返回多个值
# def circle_area_len(r):
#     return 3.14 * r * r, 2 * 3.14 * r
#
# circle = circle_area_len(5)
# print(circle)

#取一位小数   round()
def circle_area_len(r):
    """
    根据圆的半径，计算圆的面积和周长
    :param r:   升温
    :return:   圆的面积    圆的周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

circle = circle_area_len(5)
print(circle)

