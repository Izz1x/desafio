def primes_up_to_n(n): # 1
    if not isinstance(n, int) or n <= 1:
        raise ValueError("O input deve ser um número inteiro maior que 1.")

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for x in range(2, n + 1):
        if is_prime(x):
            primes.append(x)
    return primes

def primes_recursive(n, current=2, primes=None): # 2
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    if primes is None:
        primes = []
    if current > n:
        return primes

    def is_prime(num, divisor=2):
        if num < 2:
            return False
        if divisor * divisor > num:
            return True
        if num % divisor == 0:
            return False
        return is_prime(num, divisor + 1)

    if is_prime(current):
        primes.append(current)
    return primes_recursive(n, current + 1, primes)


def primes_sieve(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    primes = []
    for x in range(2, n + 1):
        if is_prime[x]:
            primes.append(x)

    return primes


print(primes_up_to_n(10))
print(primes_recursive(10))
print(primes_sieve(10))