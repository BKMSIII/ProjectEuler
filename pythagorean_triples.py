#!usr/bin/python3

# Find a, b, c where a^2 + b^2 = c^2 and a + b + c = 1000

def find_pythag_triple():
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if (a**2 + b**2) == c**2 and (a + b + c) == 1000:
                    return a, b, c
print(find_pythag_triple())
