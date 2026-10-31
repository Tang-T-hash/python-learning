# #打印十遍人生苦短，我用python
# i = 0
# while i < 10:
#     print("人生苦短，我用python")
#     i += 1
# else:
#     print("打印结束")


#计算1-100之间的偶数累加和
sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print(f"1-100的累加和为：{sum}")
