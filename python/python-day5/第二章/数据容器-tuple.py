# #元组   tuple
# # 定义
# t1 = (80, 95, 78, 50, 76, 80, 85, 20)
#
# print(t1)
# print(type(t1))
#
# print(t1[0])
# print(t1[-1])
#
# print(t1[0:5:1])
#
# # count() 统计元素的个数
# print(t1.count(80))
#
# # index() 获取元素的索引（）第一个元素的位置
# print(t1.index(80))
#
# t2 = ()
# print(type(t2))
#
# #注意：如果定义单元素的元组，单个元素之后需要加上逗号，比如(100,)
# t3 = (100,)   #错误：t3 = (100)
# print(type(t3))


# #元组 tuple 组包与解包
# t1 = (5, 7, 9, 10, 2, 23, 12)
# t2 = 5, 7, 9, 10, 2, 23, 12  #建议第一种写法
# print(t1)
# print(t2)
#
# a, b, c, d, e, f, g = t1
# print(a, b, c, d, e, f, g)
#
# print("---------------------------------")
# first, second, *other, last = t1
# print(first, second)
# print(*other)
# print(last)
#
# print("---------------------------------")
#
# *other, last2, last1 = t1
# print(*other)
# print(last2)
# print(last1)
#
# print("---------------------------------")
#
# a = 10
# b = 20
# a, b = b, a
# print(a, b)
#
# print("---------------------------------")
#
# a = 10
# b = 20
# c = 30
# a, b, c = c, b, a
# print(a, b, c)
#
#
# print("---------------------------------")




# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
# 2.统计各科成绩的最低分、最高分、平均分，并输出。
# 3.查找成绩优秀（平均分大于90）的学生，并输出。
# students = (
#     ("S001", "王林", 85, 92, 78),
#     ("S002", "李慕婉", 92, 88, 95),
#     ("S003", "十三", 78, 85, 82),
#     ("S004", "曾牛", 88, 79, 91),
#     ("S005", "周轶", 95, 96, 89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S009", "许木", 86, 89, 98),
#     ("S010", "遁天", 66, 59, 72)
# )
#
# print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# # 1.计算每个学生的总分、各科平均分，然后一并输出出来。    {avg:.1f}  保留一位小数
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
# print("---------------------------------")
# # 2.统计各科成绩的最低分、最高分、平均分，并输出。
# chinese_scores = [s[2] for s in students]
# math_scores = [s[3] for s in students]
# english_scores = [s[4] for s in students]
# print(f"语文最低分：{min(chinese_scores)}, 语文最高分：{max(chinese_scores)}, 语文平均分：{sum(chinese_scores)/len(chinese_scores)} ")
# print(f"数学最低分：{min(math_scores)}, 数学最高分：{max(math_scores)}, 数学平均分：{sum(math_scores)/len(math_scores)} ")
# print(f"英语最低分：{min(english_scores)}, 英语最高分：{max(english_scores)}, 英语平均分：{sum(english_scores)/len(english_scores)} ")
# print("---------------------------------")
#
# # 3.查找成绩优秀（平均分大于90）的学生，并输出。
# print("优秀学生(平均分 > 90)")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"学号：{s[0]}, 姓名：{s[1]}, 平均分：{avg:.1f}")


#优化
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# 1.计算每个学生的总分、各科平均分，然后一并输出出来。    {avg:.1f}  保留一位小数

#元组解包##############################################
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")

print("---------------------------------")
# 2.统计各科成绩的最低分、最高分、平均分，并输出。
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文最低分：{min(chinese_scores)}, 语文最高分：{max(chinese_scores)}, 语文平均分：{sum(chinese_scores)/len(chinese_scores)} ")
print(f"数学最低分：{min(math_scores)}, 数学最高分：{max(math_scores)}, 数学平均分：{sum(math_scores)/len(math_scores)} ")
print(f"英语最低分：{min(english_scores)}, 英语最高分：{max(english_scores)}, 英语平均分：{sum(english_scores)/len(english_scores)} ")
print("---------------------------------")

# 3.查找成绩优秀（平均分大于90）的学生，并输出。
print("优秀学生(平均分 > 90)")

#元组解包#############################################
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号：{id}, 姓名：{name}, 平均分：{avg:.1f}")