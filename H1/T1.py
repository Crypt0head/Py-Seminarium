# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

i = int(input("Input digit: "))
if i>5 and i<8:
    print("Yes")
else:
    print("No")