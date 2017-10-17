def sum_squares(n):
    # Return sum of square values in range(1, n)

    sum_sq = 0
    for i in range(1, n+1):
        sum_sq += i ** 2
    return sum_sq

def square_sum(n):
    # Return square of sum of values in range (1, n)

    sq_sum = 0
    for i in range(1, n+1):
        sq_sum += i
    sq_sum = sq_sum ** 2
    return sq_sum

def square_sum_diff(n):
    answer =  sum_squares(n) - square_sum(n)
    return answer

print abs(square_sum_diff(100))
