# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
from decimal import *

getcontext().rounding = ROUND_DOWN
TWOPLACES = Decimal(10) ** -2

A = [int(x) for x in input("Input A: ").split()]
B = [int(x) for x in input("Input B: ").split()]

print("Distance: {0}".format(Decimal(sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)).quantize(TWOPLACES)))
