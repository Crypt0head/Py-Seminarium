# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def list_num_gen(n):
    res=[]
    for i in range(0,n):
        res.append(random.randint(0, 100))
    print("List: {}".format(res))
    return res

def mult_of_pairs(vlist):
    fit = 0
    bit = len(vlist)-1
    res = []
    while(fit<=bit):
        res.append(vlist[fit]*vlist[bit])
        fit+=1
        bit-=1
    return res

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(mult_of_pairs(list_num_gen(n)))
    break