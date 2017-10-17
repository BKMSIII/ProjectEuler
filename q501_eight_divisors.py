#!usr/bin/python3

# Project Euler
# Q501. Eight Divisors

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
count = 0
for i in range(1, 10 ** 12):
    if len(factors(i)) == 8:
        count += 1
print(count)
