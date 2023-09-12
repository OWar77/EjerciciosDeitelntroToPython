"""
3.12 (Triangles) 
In an equilateral triangle, the lengths of all three sides are equal. Con-
sequently, it is also equiangular with all three internal angles congruent to each other and
measuring 60°. Write a script where a user can input the length of the three sides of a tri-
angle. The script should determine if it is an equilateral triangle or not. 
"""
lados = []
for lado in range(1,4):
    lados.append(float(input(f'Introduce la medida del lado {lado}: ')))
print(lados)
if lados[0] == lados[1] and lados[0] == lados[2]:
    print('Este triangulo tiene los 3 lados iguales')
else:
    print('Este triangulo tiene lados desiguales')