def is_fibonacci_number(num):
    import math
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

print("Is 21 a Fibonacci Number?", is_fibonacci_number(21))
