#匿名函数
# def out_line():
#     print("-------------------------")
# out_line()

# out_line = lambda : print("------------------")
# out_line()

# def add(x, y):
#     return x + y
# print(add(4, 6))
#
# add = lambda x, y: x + y
# print(add(4, 6))


#完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序：
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)
#
# data_list.sort(key=lambda  item: len(item))   #匿名函数典型的应用场景
# print(data_list)



#案例1  计算n的阶乘
#递归调用(先层层递进，再逐层回归)  指的是在函数中自己调用自己的情况   一定得有终结点
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n - 1)
#
# result = jc(10)
# print(result)





"""
案例2: 定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
  具体规则如下：
      1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
      2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""

def calc_order_cost(*args, coupon = 0, score = 0, express = 0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠卷
    :param score:  积分
    :param express:  运费
    :return:  订单总金额
    """
    # 1 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    if total_cost > 5000 and coupon <= total_cost:
        total_cost -= coupon

    if total_cost > 5000 and score // 100 <= total_cost:   #抵扣金额不能超过商品总价  // 是整除，4050 分也只抵 40 元，50 分零头自动舍掉
        total_cost -= score // 100

    total_cost += express
    return total_cost


# print(calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 3999, 1), coupon=10, score=4000, express=9.9))

# print(calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 7999, 1), coupon=10, score=4000, express=9.9))

total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 3999, 1), express=9.9)
print(total)