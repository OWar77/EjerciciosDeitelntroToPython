"""
4.10 (Guess the Number) Write a script that plays “guess the number.” Choose the
number to be guessed by selecting a random integer in the range 1 to 1000. Do not reveal
this number to the user. Display the prompt "Guess my number between 1 and 1000 with
the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display
"Too high. Try again." or "Too low. Try again." as appropriate to help the player “zero
in” on the correct answer, then prompt the user for the next guess. When the user enters
the correct answer, display "Congratulations. You guessed the number!", and allow the
user to choose whether to play again. 
"""
import random

#Determina el numero aleatorio
x = random.randrange(1,1001)

#Primera lectura del numero del usuario
miNumero = int(input("Ingresa el número que crees que tengo entre 1 y 1000\n"))
contador = 1
#ciclo para leer y comparar
while x != miNumero:
    if miNumero > x:
        print("Estas mal, tu número es MAYOR que el mío\n")
        miNumero = int(input("Adivina de nuevo!!!\n"))
        contador += 1
    elif miNumero < x:
        print("Estas mal, tu número es MENOR que el mío\n")
        miNumero = int(input("Adivina de nuevo!!!\n"))
        contador += 1
#Al ser iguales se sale del ciclo
print(f'Felicidades, adivinaste mi número en {contador} intentos!!!\n')
    