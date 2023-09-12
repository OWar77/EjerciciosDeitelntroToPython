"""
3.28 (Intro to Data Science: Mean, Median and Mode) Calculate the mean, median, and
mode of the temperatures measured in Sidney on the first 9 days of February (in °C): 19.5,
19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2 and 19.5. Suppose 20.2°C is measured on day 10
and added to the dataset. What problem might occur? 
"""
import numpy as n
from scipy import stats as s

temp = [19.5,19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2,19.5]

print(f'Temperaturas: {temp}')
print(f'Mediana o valor promedio: {n.mean(temp)}')
print(f'Media: {n.median(temp)}')
ordtemp=sorted(temp)
print(f'Valores ordenados: {ordtemp}')
print(f'Moda: {s.mode(temp,keepdims=False)}')
print('\n\nOtro dia de 20.2°')
temp.append(20.2)
print(f'Temperaturas: {temp}')
print(f'Mediana o valor promedio: {n.mean(temp)}')
print(f'Media: {n.median(temp)}')
ordtemp=sorted(temp)
print(f'Valores ordenados: {ordtemp}')
print(f'Moda: {s.mode(temp,keepdims=False)}')

