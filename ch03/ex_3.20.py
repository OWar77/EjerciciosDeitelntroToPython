print("""
3.20 (Binary-to-Decimal Conversion) Input an integer containing 0s and 1s (i.e., a “bi-
nary” integer) and display its decimal equivalent. The online appendix, “Number Systems,”
discusses the binary number system. [Hint: Use the modulus and division operators to pick
off the “binary” number’s digits one at a time from right to left. Just as in the decimal num-
ber system, where the rightmost digit has the positional value 1 and the next digit to the left
has the positional value 10, then 100, then 1000, etc., in the binary number system, the
rightmost digit has the positional value 1, the next digit to the left has the positional value
2, then 4, then 8, etc. Thus, the decimal number 234 can be interpreted as 2 * 100 + 3 *
10 + 4 * 1. The decimal equivalent of binary 1101 is 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.]
""")

bin = input('Digite su numero binario, solo 0 y 1: ')
potencia = 0
eq = ''
valor = 0
for bit in reversed(bin):
    if (bit != '0') and (bit != '1') :
        print('Solo se perminten 0 y 1 en el valor binario.')
        print(f'bit: {bit}')
        exit()
    eq += f'({bit} x {2**potencia})'
    valor += int(bit) * (2**potencia)
    if potencia+1 < len(bin):
        eq += ' + '
    potencia += 1    
    
print(f'{bin} equivale a: {valor}')
print(f'Desarrollo: {eq}')