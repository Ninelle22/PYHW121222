#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#for x in range(2):
#   for y in range(2):
#       for z in range(2):
#           print((not(x or y or z) == (not(x) or not(y) or not(z))))


#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3


p = list(map(int, input("Enter coordinates X and Y: ").split(" ")))
if p[x] != 0 and p[y] != 0:
    if p[x] < 0:
        if p[y] > 0:
            print(f"Point with coordinates ({p[x]}, {p[y]}) locates in 2 quarter")
        else:
            print(f"Point with coordinates ({p[x]}, {p[y]}) locates in 3 quarter")
    else:
        if p[y] > 0:
            print(f"Point with coordinates ({p[x]}, {p[y]}) locates in 1 quarter")
        else: 
            print(f"Point with coordinates ({p[x]}, {p[y]}) locates in 4 quarter")
        
        
        

        
  
