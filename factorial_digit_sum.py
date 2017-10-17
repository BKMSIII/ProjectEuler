#!usr/bin/python3

def sum_digits_factorial(n):
    count = 0
    product = 1
    for i in range(1, n + 1):
        product = product * i
    for i in str(product):
        count += int(i)
    return count

print(sum_digits_factorial(100))
