#!usr/bin/python3

def collatz_sequence(n):
    chain = 1
    while n != 1:
        if n % 2 == 0:
            n = pos_collatz(n)
            chain += 1
            if n == 1:
                return chain
        if n % 2 == 1:
            n = neg_collatz(n)
            chain += 1
            if n == 1:
                return chain
def neg_collatz(n):
    return 3 * n + 1

def pos_collatz(n):
    return n /2


maxChainLength = 0
maxChainValue = 0
for i in range(1, 1000001):
    chainLength = collatz_sequence(i)
    if chainLength > maxChainLength:
        maxChainLength = chainLength
        maxChainValue = i
print(maxChainValue)
