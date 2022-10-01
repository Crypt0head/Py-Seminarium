# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x, y = input("Input dot coordinates: ").split()

x = int(x)
y = int(y)

if x == 0:
    print("Dot on 0Y axis")

if y == 0:
    print("Dot on 0X axis")

if x>0:
    if y>0:
        print(1)
    elif y<0:
        print(4)
elif x<0:
    if y>0:
        print(2)
    elif y<0:
        print(3)