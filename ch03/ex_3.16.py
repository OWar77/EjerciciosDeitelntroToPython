"""
3.16 (Fastest Runners) Use a loop to find the fastest and second fastest from 10 runners
whose speeds are entered. The speed of each runner is entered by the user in m/sec.
"""
vels = []
for x in range(1,11):
    vels.append(int(input(f'Velocidad en m/seg para el corredor {x}: ')))
vels.sort(reverse=True)
pos = 0
for vel in vels:
    if pos == 0:
        print(f'El corredor más rápido corre a {vel} m/seg.\n')
    elif pos == 1:
        print(f'El corredor en segundo lugar corre a {vel} m/seg.')
    else:
        break
    pos += 1
print(f'Done!!!!')
