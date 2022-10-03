# Реализуйте алгоритм перемешивания списка.

import random

def list_num_gen(n):
    res=[]
    for i in range(0,n):
        res.append(random.randint(0, 100))
    print("List: {}".format(res))
    return res

def shuffle(num_list):
    index_set = set()
    count = len(num_list)
    mv_index = random.randint(0, count-1)
    for i in range(0, int(count/2)):
        while(mv_index in index_set or mv_index == i):
            mv_index = random.randint(0, count-1)
        index_set.add(mv_index)
        tmp = num_list[i]
        num_list[i]=num_list[mv_index]
        num_list[mv_index]=tmp
    return num_list  

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print("Shuffled List: {}".format(shuffle(list_num_gen(n))))
    break