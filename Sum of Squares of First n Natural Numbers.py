def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

print("Sum of squares of first 5 natural numbers:", sum_of_squares(5))
