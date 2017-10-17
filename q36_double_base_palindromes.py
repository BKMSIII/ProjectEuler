#!usr/bin/python3

# Project Euler
# Q36. Double base palindromes

count  = 0

for num in range(10 ** 6):
    if str(num) == str(num)[::-1]:
        binary = bin(num)[2:]
        if binary == binary[::-1]:
            count += num

print(count)
