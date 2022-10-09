import random
L1 = random.sample(range(1, 271), 90)     # 生成学号
"""
L2 = random.sample(range(1, 271), 90)
L3 = random.sample(range(1, 271), 90)
L4 = random.sample(range(1, 271), 90)
L5 = random.sample(range(1, 271), 90)
"""
print(L1, end="\n")
"""
print(L2, end="\n")
print(L3, end="\n")
print(L4, end="\n")
print(L5, end="\n")
"""
c = [[0] * 20 for _ in range(90)]     # c[i]为第i位同学的出勤情况，1代表缺勤，0代表出勤
absentNum = random.randint(5, 8)   # 经常缺席人数
absent_ord = random.sample(range(90), absentNum)   # 经常缺席的学生序号 0-89
print("经常缺席的学生序号及学号：")
for i in absent_ord:
    print(i, ' ', L1[i], end="\n")
temp = list(i for i in range(90))
for i in absent_ord:
    temp.remove(i)  # 剔除经常缺席学生学号
    absenttime = random.sample(range(20), 16)
    for j in absenttime:
        c[i][j] = 1  # 标记经常缺席的学生缺席课次
for i in range(20):  # 第i节课
    a = random.randint(0, 3)  # 缺席人数（偶尔）
    absentCal = random.sample(temp, a)  # 缺席学生学号
    for j in absentCal:
        c[j][i] = 1
for i in range(90):
    print(c[i], end="\n")