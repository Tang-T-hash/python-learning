#商品类
class Goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num


    def __str__(self):
        return f"商品名称：{self.name} - 商品价格：{self.price} - 商品数量：{self.num}"


    def update_Goods(self, name, price, num):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num



#购物车系统
class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车系统"

    def __init__(self):
        self.goods_list = []


    #添加
    def add_Goods(self):
        name = input("请输入商品名称：")
        for s in self.goods_list:
            if s.name == name:
                print("添加失败，商品已存在")
                return

            price = int(input("请输入商品价格："))
            num = int(input("请输入商品数量："))

            if price > 0 and num > 0:
                goods_info = Goods(name, price, num)
                self.goods_list.append(goods_info)
                print("商品信息添加成功！")
            else:
                print("商品价格和数量必须大于0！")


    #修改
        def update_Goods(self):
            name = input("请输入商品名称：")
            for s in self.goods_list:
                if s.name == name:
                    print(f"当前商品信息：{s}")

                    price = int(input("请输入商品价格："))
                    num = int(input("请输入商品数量："))

                    if price > 0 and num > 0:
                        s.update_score(price, num)
                        print("商品信息修改成功！")
                        print(f"修改后的购物车：{s}")
                        return
                    else:
                        print("价格和数量必须大于0！")
                        return

            print("未找到该商品，修改失败！")


    #删除
        def delete_Goods(self):
            name = input("请输入要删除商品的名称：")
            for s in self.goods_list:
                if s.name == name:
                    self.goods_list.remove(s)
                    print("商品信息删除成功！")
                    return
            print("未找到该商品，删除失败！")

    #查询
        def list_Goods(self):
            for s in self.goods_list:
                print(s)


    # 运行系统
            def run(self):
                print(f"欢迎使用购物车系统 V {ShoppingCart.system_version}")

                while True:
                    print()
                    print("#########################################################################")
                    print("#1.添加商品  2.修改商品  3.删除商品  4.查询所有商品  5.退出系统#")
                    print("#########################################################################")
                    print()

                    choice = input("请选择你要进行的操作1-5:")
                    match choice:
                        case "1":
                            self.add_Goods()
                        case "2":
                            self.update_Goods()
                        case "3":
                            self.delete_Goods()
                        case "4":
                            self.query_Goods()
                        case "5":
                            break  # 退出系统
                        case _:
                            print("输入错误，请选择1-5！！")

        if __name__ == '__main__':
            shopping_cart = ShoppingCart()
            shopping_cart.run()