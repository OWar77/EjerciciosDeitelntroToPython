"""
3.13 (Perfect Numbers) In number theory, a perfect number is a positive integer that is
equal to the sum of its divisors. Perfect numbers were first studied by the Pythagoreans
who thought that they had mystical properties. They were also extensively studied by
Greeks (including Euclid) for their numerological properties.
The smallest perfect number is 6, because 6 = 3 + 2 + 1, with 3, 2, and 1 being the divi-
sors. Other examples of perfect numbers are: 28, 496 and 8128. Write a script that inputs
a nonnegative integer and displays whether it is a perfect number or not.
"""
# Algoritmo Numero_prefecto

#                Definir n,x,perfecto Como Entero
num = int(input('Dame un numero entero: '))
x = 2
perfecto = 0
while x <= num:
    if num % x == 0:
        perfecto += num/x
    x += 1
if perfecto == num:
    print(f'El número {num} es un número perfecto')
else:
    print(f'El número {num} no es un número perfecto')
