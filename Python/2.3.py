def prime_factors(n):

    factors = []
    d = 2

    while n > 1:

        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1

    return factors


n = 56

print(prime_factors(n))
