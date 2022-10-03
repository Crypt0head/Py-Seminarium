# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def list_num_gen(n):
    res=[]
    for i in range(0,n):
        res.append(format(random.uniform(0, 20), ".2f"))
    print("List: {}".format(res))
    return res

def diff(vlist):
    min = float(vlist[0])
    max = float(0)
    for i in vlist:
        tmp = float(i)%1
        if min>tmp:
            min = tmp
        elif max<tmp:
            max = tmp
    print("Max: {0} \nMin: {1}".format(format(max, ".2f"), format(min, ".2f")))
    return format(max-min, ".2f")

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(diff(list_num_gen(n)))
    break