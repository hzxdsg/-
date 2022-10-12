import random
def create_id():
    L = []
    for i in range(5):
        Le= random.sample(range(1, 271), 90)  # 生成学号
        L.append(Le)
    return L

def main():
    id = create_id()
    for i in range(5):
        print(id[i])

main()