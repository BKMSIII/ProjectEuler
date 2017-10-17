#!usr/bin/python3

def power_digit_sum(n):
    sum = 0
    prod = n ** 1000
    for i in str(prod):
        sum += int(i)
    return sum

print(power_digit_sum(2))
