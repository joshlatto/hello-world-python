print("Hello world!")

def find_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        print("Current number:", n)
        print("Divisor:", divisor)
        while n % divisor == 0:
            factors.append(divisor)
            print(factors)
            n //= divisor
            print("Current number:", n)
            print("Divisor:", divisor)
        divisor += 1
    return factors

print("Prime factors of 56:", find_prime_factors(56))