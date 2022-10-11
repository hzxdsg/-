import random
#以序列seq中值出现的概率来随机生成某个值
def rand_pick(seq , probabilities):
    x = random.uniform(0 ,1)
    cumprob = 0.0
    for item , item_pro in zip(seq , probabilities):
        cumprob += item_pro
        if x < cumprob:
            break
    return item
value_list = [0 , 1]
probabilities = [0.4 , 0.6]
print(rand_pick(value_list, probabilities))