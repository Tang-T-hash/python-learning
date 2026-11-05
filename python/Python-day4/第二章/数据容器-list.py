# # list
#
# s = [56, 54, 66, 98, 36, "A", "Hello", True]
#
# print(type(s))
#
# # 获取
#
# print(s[0])   #正向索引 从0开始
# print(s[-8])  #反向索引  从-1开始
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# #删除
# del s[6]
# print(s)
#
#
# # list切片
# s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#
# # 切片操作  s[开始索引：结束索引：步长]
# print(s[:5])   # print(s[0:5:1])    #print(s[:5:1])   #print(s[:5:])
#
# print(s[0:-2:1])
# print("-------------------")
#
# b = [43, 54, 65, 66, 34, 25, 90, 66]
# b.append(78)
# print(b)
#
# b.insert(1, 11)
# print(b)
#
# b.remove(66)
# print(b)
#
# b.pop(3)
# print(b)
#
# b.sort()
# print(b)
#
# b.reverse()
# print(b)




# num_list = []
# for i in range(10):
#     num = int(input("请输入十个有效的数字："))
#     num_list.append(num)
#
# print("数字列表：", num_list)
#
# num_list.sort()
# print("排序后的数字列表", num_list)
#
# print("最小值：", num_list[0])
# print("最大值：", num_list[-1])
# print("平均值：", sum(num_list)/len(num_list))   #sum()求和    len()列表的长度
#
# print(min(num_list))   #最小值
# print(max(num_list))   #最大值



# 案例
# num_list1 = [19, 23, 43, 53, 25, 67, 54, 66, 23, 100]
# num_list2 = [19, 22, 42, 54, 67, 66, 78, 99]
#
# for num in num_list2:
#     num_list1.append(num)
# print("合并后的原始列表：", num_list1)
#
# num_list = []
# for num in num_list1:
#     if num not in num_list:
#         num_list.append(num)
#
# print("去重复后的列表：", num_list)



#案例  简化
# num_list1 = [19, 23, 43, 53, 25, 67, 54, 66, 23, 100]
# num_list2 = [19, 22, 42, 54, 67, 66, 78, 99]
# #解包: 将列表这一类容器解开成一个独立的元素
# # 闭包：将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
#
# print("合并后的原始列表：", num_list1)
#
# num_list = []
# for num in num_list1:
#     if num not in num_list:
#         num_list.append(num)
#
# print("去重复后的列表：", num_list)


#简化
# num_list1 = [19, 23, 43, 53, 25, 67, 54, 66, 23, 100]
# num_list2 = [19, 22, 42, 54, 67, 66, 78, 99]
# num_list = num_list1 + num_list2
#
# print("合并后的原始列表：", num_list)
#
# num_list = []
# for num in num_list1:
#     if num not in num_list:
#         num_list.append(num)
#
# print("去重复后的列表：", num_list)

#传统方式
# num_list = []
# for i in range(1, 21):
#     num_list.append(i**2)
# print(num_list)
#
# #列表推导式  [要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1, 21)]
# print(num_list2)



# #列表推导式   [for i in 序列/列表 if 条件]
# num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
# new_list = [i**2 for i in num_list if i % 2 == 0]
# print(new_list)


#练习1
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I','J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# list = list1 + list2 + list3
# print("合并后：" ,list)
#
# list = []
# for i in list1:
#     if i not in list:
#         list.append(i)
# for i in list2:
#     if i not in list:
#         list.append(i)
# print("去除重复后：", list)
#
# list.sort()
# print("排序后：", list)

#练习二
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30]
# list = [i**2 for i in list1 if i % 5 == 0 or i % 3 == 0]
# print(list)


#练习三
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list = [i for i in list1 if i > 0]
print(list)