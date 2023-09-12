print("""
3.21 (Calculate Distance in m, dm, cm and mm) A trainer wants to calculate the addi-
tional distance an athlete needs to jump to break the world record for the longest long
jump (8.85 m). Write a script that accepts the current jumping distance of the athlete in
meters as input. Display the difference in distance between the world record and the cur-
rent jump in m, dm, cm, and mm. For example, when an athlete jumps 6.43 m, the script
would output:
You need to jump: 2.42 additional meters to improve the world record.
Meters: 2.0
Decimeters: 4.0
Centimeters: 2.0
Millimeters: 0.0
""")

dist = float(input('Distancia del salto en metros, para batir el record de 8.85:   '))
goal = 8.85
diff = goal - dist
print(f'{diff}')
mt = int(diff)
dm = int((diff-mt)*10)
cm = int((diff-mt)*100)-(dm*10)

print(f'mt = {mt}')
print(f'dm = {dm}')
print(f'cm = {cm}')
