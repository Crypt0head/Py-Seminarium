# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def list_num_gen(n):
    res=[]
    for i in range(0,n):
        res.append(random.randint(0, 100))
    print("List: {}".format(res))
    return res

def sum_of_odd(vlist):
    it = 1
    res = 0
    while(it<len(vlist)):
        res+=vlist[it]
        it+=2
    return res

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(sum_of_odd(list_num_gen(n)))
    break