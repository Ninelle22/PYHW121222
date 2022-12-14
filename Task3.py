# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

#number = int(input("Enter number of the quarter: "))
#if number == 1:
 #   print("x > 0; y > 0")
#elif number == 2:
 #   print("x < 0; y > 0")
#elif number == 3:
 #   print("x < 0; y < 0")
#elif number == 4:
 #   print("x < 0; y < 0")
    
#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21 

# distance = sqrt((x1-x2)**2+(y1-y2)**2)

import math
A = list(map(float, input("Enter coordinates X and Y: ").split(" ")))
B = list(map(float, input("Enter coordinates X and Y: ").split(" ")))
d = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
d = int(d * 100)
print(f"Distance between A and B in 2D =>> {float(d / 100)}")

