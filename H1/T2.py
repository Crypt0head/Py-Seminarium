# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений  предикат.

x, y, z = input("Input three predicates x, y, z: ").split()

print(not (x and y and z) == ( not x or not y or not z))
