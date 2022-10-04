# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def f(n):
    res=[]
    prev =1
    for i in range(1, int(n)+1):
        prev*=i
        res.append(prev)
    return res

while True:
    n = input("Enter number: ")
    try:
        int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(f(n))
    break