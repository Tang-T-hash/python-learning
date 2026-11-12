# 变量定义 - 未指定类型注解 ---> 类型推断
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E", 100]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods = ("手机", 6999, 1)



# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int | float] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count":2 , "total":10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append("X")
names2.append(10010)
names2.append(10010.0)



# 函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


al = circle_area_len(9.5)
print(al)





def calc_order_cost(*args:tuple[str, float, int], coupon:int = 0, score:int = 0, express:float = 0.0) -> float:
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



total = calc_order_cost(("鼠标", 88.5, 2),("键盘", 388, 1),("手机", 3999, 1), express=9.9)
print(total)