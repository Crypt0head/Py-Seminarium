# Напишите программу, которая по заданному номеру четверти, 

# показывает диапазон возможных координат точек в этой четверти (x и y).

i = int(input("Input digit: "))

if i == 1:
    print("(0...INF, 0...INF)")
if i == 2:
    print("(0...-INF, 0...INF)")
if i == 3:
    print("(0...-INF, 0...-INF)")
if i == 4:
    print("(0...INF, 0...-INF)")