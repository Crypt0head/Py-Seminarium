# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def sum_of_list(n):
    l = []
    sum = 0
    for i in range(1, n+1):
        l.append(round((1+1/i)**i))
        sum+=l[i-1]
    print("List: {}".format(l))
    return sum

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(sum_of_list(n))
    break