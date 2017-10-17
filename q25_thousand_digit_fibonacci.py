#!usr/bin/python3

# Project Euler
# Q25. 1000 digit Fibonacci sequence

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b

for index, fibonacci_number in enumerate(fib()):
     if len(str(fibonacci_number)) >= 1000:
         print index
         break
