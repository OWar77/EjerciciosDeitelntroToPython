"""
3.7 (Table of Bacteria) 
Starting with 200 bacteria, the growth in the
number of bacteria after n hours is calculated as follows: B = 200 × 2´n. Print the number
of bacteria after 0,  5, 10, and 15 hours in table format as shown below.
"""
horas = [0,5,10,15,20,25,30]
IniBac = 200
print('Hora     Número de bacterias')
for t in horas:
    B = IniBac * (2 ** t)
    print(f'{t:>2}      {B:>20}')
