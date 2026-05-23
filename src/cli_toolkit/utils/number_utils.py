def is_even_or_odd(n):
    if n % 2 == 0:
        return "even"
    return "odd"


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
