"""
3.9 (Calculating Time)

    2.11 (Calculating Time) Write a script that inputs a number of seconds from the user.
    Calculate the number of hours, minutes, and remaining seconds. Print them separated by
    “ - ”. For example, if the user types 3750 seconds as input, the script should print: 
    1 - 2 - 30
    Assume that the user enters a number of seconds that is higher than 3600. Use both the floor
    division and the remainder operation to calculate the number of hours, minutes, and seconds.

In Exercise 2.11, you wrote a script that calculated the number
of  hours,  minutes,  and  remaining  seconds  based  on  the  number  of  seconds  received
through user input. Reimplement your script to use a loop that in an iterative process
“picks off” the hours, minutes, and remaining seconds using the // and % operators
"""

segundos = int(input(f'Introduzca número de segundos: '))
horas = segundos // 3600
minutos = (segundos%3600) // 60
secs = segundos - (horas * 3600) - (minutos * 60)
print(f'{horas} - {minutos} - {secs}')
