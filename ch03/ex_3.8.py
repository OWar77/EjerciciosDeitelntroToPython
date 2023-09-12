"""
3.8 (Flu Patients Data Processing)
During the flu season, it is important to keep track
of the number of infected patients. Write a script in which the user can input the number
of reported infections per day over one week. Calculate the total, average, smallest, and
largest of these values. Write your script using a loop structure.
"""
total = 0
# infected per day - ipd
ipd = []
for i in range(1,8):
    numinfected = int(input(f'Número de infectados el día {i}: '))
    ipd.append(numinfected)
    total += numinfected
print(f'Los valores recolectados son: {ipd}')
print(f'El promedio de los valores es: {(sum(ipd)/len(ipd)):>.2f}')
print(f'El valor minimo de estos valores es: {min(ipd)}')
print(f'El valor máximo de estos valores es: {max(ipd)}')