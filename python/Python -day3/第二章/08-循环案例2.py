# import random
# random_num = random.randint(1, 100)
#
# while True:
#     num = int(input("请输入一个数字："))
#     if num > random_num:
#         print("猜大了")
#         continue
#     elif num < random_num:
#         print("猜小了")
#         continue
#     else:
#         print("恭喜您猜对了！")
#         break
# print(f"随机数字是：{random_num}")



# sum = 0
# for i in range(1, 1001):
#     if i % 5 == 0:
#         sum += i
# print(sum)


num = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
a = 0
k = 0
for c in num:
    if c == "a":
        a += 1
    elif c == "k":
        k += 1
print(f"一共有{a}个k, {k}个k")

