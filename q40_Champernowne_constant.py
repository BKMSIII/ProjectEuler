#!usr/bin/python3

# Project Euler# Q40. Champernowne's constant

dec = ''

for i in range(1, 500000): # Generate
    dec += str(i)

answer = int(dec[0]) * int(dec[9]) * int(dec[99]) * int(dec[999]) * int(dec[9999]) * int(dec[99999]) * int(dec[999999])
print(answer)
