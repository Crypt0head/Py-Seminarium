# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibo(value):
    pres = [0, 1]
    nres = [0, 1]
    next = 1
    prev = 0
    while next<value:
        pres.append(pres[next]+pres[prev])
        nres.append(nres[prev]-nres[next])
        next+=1
        prev+=1
    nres = nres[::-1]
    nres.pop()
    nres.extend(pres)
    return nres

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(fibo(n))
    break