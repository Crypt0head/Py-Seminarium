# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum_of_digits(str, isNeg):
    res=0
    for i in range(0+int(isNeg), len(str)):
        if str[i] != '.':
            res+=int(str[i])
    return res

while True:
    str = input("Enter float number: ")
    isNeg = False
    try:
        if float(str) < 0:
            isNeg = True
    except:
        print("Wrong input, float number expected")
        continue
    print(sum_of_digits(str, isNeg))
    break
