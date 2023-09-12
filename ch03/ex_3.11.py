"""
3.11 (Rabbit Births)
A farmer wants to keep track of the average number of rabbits born
on his farm every month. He records the number of does (female rabbits) he has combined
with  the  number  rabbits  born  every  month.  Develop  a  sentinel-controlled-repetition
script that prompts the user to input the number of does living in the farm and the number
of rabbits born in a specific month. After processing all input information, the script
should calculate and display the combined average number of rabbits born per doe.
"""
hembras = 0
while hembras != -1:
    hembras = int(input('Ingrese el número de hembras en la colonia de conejos: '))
    conejitos = int(input('Conejitos nacidos el mes pasado: '))
    if hembras != 0:
        print(f'En promedio {conejitos/hembras:.2f} conejitos nacieron por cada hembra')
    else:
        print(f'No hubo hembras el mes pasado :(')