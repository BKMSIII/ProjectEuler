#!usr/bin/python3

# Project Euler
# Q24 Lexographic permutations

from itertools import permutations

a = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # Create list from permutation generator
print(a[999999]) # Print millionth object
