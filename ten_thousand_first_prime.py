#!usr/bin/python3
# Find the 10001st prime number

def find_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return None
    return True
def find_n_prime(n):
    primes_found = 0
    count = 2
    while primes_found < n:
            if find_prime(count) == True:
                primes_found += 1
                print count, primes_found
            count += 1
    return count

#print(find_n_prime(10001))
print(find_n_prime(10001))
