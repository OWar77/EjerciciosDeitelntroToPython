"""
4.9 (Temperature Conversion) Implement a fahrenheit function that returns the
Fahrenheit equivalent of a Celsius temperature. Use the following formula:
F = (9 / 5) * C + 32
Use this function to print a chart showing the Fahrenheit equivalents of all Celsius tem-
peratures in the range 0–100 degrees. Use one digit of precision for the results. Print the
outputs in a neat tabular format.
"""

def fahrenheit(C) :
    return ( 9 / 5 ) * C + 32

print("Celcius      Fahrenheit")
for temp in range(101):
    print(f'{temp:3}              {fahrenheit(temp):5.1f}')