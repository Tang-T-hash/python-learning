# msg = input("请输入要遍历的字符串")
# for i in msg:    # s表示遍历出来的元素   msg表示需要遍历的数组
#     print(i)
# else:
#     print("遍历结束！")



#计算1-100之间所有奇数之和
#原始写法
# sum = 0
# for i in range(1, 101):        #range(1, 100, 1)
#     if i % 2 == 1:    #奇数
#         sum += i

#简写
# sum = 0
# for i in range(1, 100, 2):
#         sum += i
#
# print(f"1-100的奇数的累加和为：{sum}")


#计算100-500 之间所有3的倍数的数字之和

# sum = 0
# for i in range(100, 501):
#     if i % 3 == 0:
#         sum += i
#
# print(f"100-500之间的3的倍数的累加和：{sum}")





# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))
#
# for i in range(n):   #控制行
#     for j in range(m):    #控制列
#         print("*",end="  ")
#     print()



#9 x 9 乘法表
# for i in range(1, 10):
#     for j in range (1, i + 1):
#         print(f"{i} x {j} = {i * j}", end="\t")
#     print()



# a = int(input("请输入直角边的边长："))
# for i in range(1,a + 1):
#     for j in range(1,i+1):
#         print(" * ", end=" ")
#     print()



# a = int(input("请输入一个数字"))
# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("&", end=" ")
    print()
