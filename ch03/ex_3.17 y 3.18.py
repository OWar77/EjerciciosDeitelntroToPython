print("""
3.17 (Nested Loops) Write a script that displays the following triangle patterns separate-
ly, one below the other. Separate each pattern from the next by one blank line. Use for
loops to generate the patterns. Display all asterisks (*) with a single statement of the form 
print('*', end='')
which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
each line with zero or more space characters.]

The patterns are:

(a)         (b)         (c)         (d)
*           **********  **********  *
**          *********   *********   **
***         ********    ********    ***
****        *******     *******     ****
*****       ******      ******      *****
******      *****       *****       ******
*******     ****        ****        *******
********    ***         ***         ********
*********   **          **          *********
**********  *           *           **********

#####################################################

Result:


""")
print('a')
for x in range (1,11):
    for y in range (0,x):
        print('*', end='')
    print('')
print('')
print('b')
for x in range (10,0,-1):
    for y in range (0,x):
        print('*', end='')
    print('')
print('')
print('c')
for x in range (10,0,-1):
    for z in range(x,10):
            print(' ',end='')   
    for y in range (0,x):  
        print('*', end='')        
    print('')
print('')
print('d')
for x in range (1,11):
    for z in range(x,10):
            print(' ',end='')   
    for y in range (0,x):  
        print('*', end='')        
    print('')

print("""
3.18 (Challenge: Nested Looping) Modify your script from Exercise 3.17 to display all
four patterns side-by-side (as shown above) by making clever use of nested for loops. Sep-
arate each triangle from the next by three horizontal spaces. [Hint: One for loop should
control the row number. Its nested for loops should calculate from the row number the
appropriate number of asterisks and spaces for each of the four patterns.] 

""")
print('(a)          (b)          (c)          (d)')
for x in range (1,11):
    for a in range(0,x):
        print('*', end='')
    for a in range(0,13-x):
        print(' ',end = '')

    for b in range (0,11-x):
        print('*', end='')
    for b in range(0,x+2):
        print(' ',end = '')
    
    for c in range(0,x-1):
        print(' ', end='')
    for c in range(0,11-x):
        print('*',end = '')

    for d in range (0,13-x):
        print(' ', end='')
    for d in range(0,x):
        print('*',end = '')    
    print('')
