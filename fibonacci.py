import math

def fibonacci_binet(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi)**(-n)) / math.sqrt(5))

def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci_binet(10))
print(fibonacci_recursive(10))
print(fibonacci_iterative(10))
