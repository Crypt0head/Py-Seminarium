# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

def list_num_gen(n):
    res=[]
    for i in range(0,n):
        res.append(random.randint((-1)*int(n), int(n)))
    print("List: {}".format(res))
    return res

def num_product(fname, num_list):
    res=1
    try:
        f = open(fname)
    except:
        print("Can't open file: {}. Does it exist?".format(fname))
        exit()
    for num in f:
        try:
            res*=num_list[int(num)]
        except:
            print("Position of {} is out of range and will be skip".format(num))
    return res

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(num_product("file.txt", list_num_gen(n)))
    break