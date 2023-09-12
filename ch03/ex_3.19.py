print("""
3.19 (Prime Factorization) A prime number is divisible only by itself and 1 (e.g., 2, 3, 5,
7, 11, 13, …). The prime factors of a number are a set of prime numbers that multiply to-
gether to result in the given number. Thus, if a number is a divider of the given number
and also a prime number, it is a prime factor of the given number. Prime factorization is
the search for all prime factors of a given number. Write a script that uses a trial and error
approach to determine the prime factors of the number 1537.
""")

num = 1537
fp = []
for x in range(1,num+1):
    if (num % x == 0):
        fp.append(x)
print(f'Los factores de {num} son: {fp}')