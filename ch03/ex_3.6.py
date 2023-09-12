"""
3.6 (Turing Test) 
Create a script that plays the part of the independent computer, giving its user a sim-
ple medical diagnosis. The script should prompt the user with 'What is your problem?'
When the user answers and presses Enter, the script should simply ignore the user’s input,
then prompt the user again with 'Have you had this problem before (yes or no)?' If
the user enters 'yes', print 'Well, you have it again.' If the user answers 'no', print
'Well, you have it now.'
"""

input('¿Qué problema tienes?: ')
SioNo = input('¿Ya habías tenido este problema antes? (si/no): ')
if SioNo=='si':
    print('Bueno, pues te volvio a dar.')
elif SioNo=='no':
    print('Pues lo tienes ahora.')
else:
    print('Debes responder si o no, en minúsculas. Por eso estas como estas!!!')
