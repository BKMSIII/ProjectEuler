#!usr/bin/python3

# Find the sum of primes below 2 milllion

def find_prime(n):
    if (n % 2) == 0:
        return None
    for i in range(2, n/2):
        if (n % i) == 0:
            return None
    return n

def find_sum_primes(n):
    prime_sum = 0
    for i in range(1, n+1):
        if find_prime(i) != None:
                primes += i
            print(primes, i)
    return primes

print(find_sum_primes(2000000))
