"""
3.14 (Challenge: Approximating the Mathematical Constant  ) Write a script that com-
putes the value of π from the following infinite series. Print a table that shows the value of
π approximated by one term of this series, by two terms, by three terms, and so on. How
many terms of this series do you have to use before you first get 3.14? 3.141? 3.1415?
3.14159?
"""
# Leemos el número de términos
term = 2*(int(input('Introduzca cuantos terminos de la serie quiere calcular para π: ')))
# Iniciamos la variable que guardará el valor de Pi y el contador de términos de la serie
pi = 0
contador = 1
# Iteramos todos los términos de la serie, comenzando en 1, hasta el número de términos
# y avanzando 2 posiciones cada vez, debido a que la serie no necesita los denominadores pares.
# También debemos recordar que en la función range() se detiene uno antes del numero superior, 
# por eso se le suma 1 al número de términos a analizar
for t in range(1,term+1,2):
    # Checamos si el contador es par o no para determinar si se suma o se resta el término actual
    if contador % 2 :
        # Si es par se suma
        pi += 4/t
    else:
        # Si es impar se resta
        pi -= 4/t
    # Imprimimos el resultado cada 100 iteraciones
    if contador%100 == 0 :
        print(f'Termino número {contador} ->    Valor de π: {pi:>.20f}')
    # Se incrementa el contador para el siguiente ciclo
    contador +=1
print(f'Para los {contador-1} elementos de la serie, el valor de π es: {pi:>.20f}')
