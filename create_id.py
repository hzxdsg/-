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
L1 = random.sample(range(1, 270), 90)
"""
L2 = random.sample(range(1, 270), 90)
L3 = random.sample(range(1, 270), 90)
L4 = random.sample(range(1, 270), 90)
L5 = random.sample(range(1, 270), 90)
"""
print(L1,end="\n")
"""
print(L2,end="\n")
print(L3,end="\n")
print(L4,end="\n")
print(L5,end="\n")
"""
absentNum=random.randint(5,8)
absent1= random.sample(L1,absentNum)
print(absent1,end="\n")