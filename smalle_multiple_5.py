#!usr/bin/python3
from fractions import gcd
from functools import reduce

def find_smallest_multiple(n):
    return reduce(lcm, range(1, n+1))

def lcm(a, b):
    return a*b//gcd(a,b)

print(find_smallest_multiple(20))
