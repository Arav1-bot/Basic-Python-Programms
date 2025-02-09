def cube_sum_of_naturals(n):
    return sum(i ** 3 for i in range(1, n + 1))

print("Cube sum of first 5 natural numbers:", cube_sum_of_naturals(5))
