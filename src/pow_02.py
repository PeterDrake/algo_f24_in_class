def power(a, n):
    """
    :return: a raised to the nth power
    """
    result = 1
    for i in range(n):
        result *= a
    return result


def power(a, n):
    print(f'power({a}, {n})')
    if n == 0:
        return 1
    if n % 2 == 0:
        r = power(a, n / 2)
        return r * r
    r = power(a, (n-1) / 2)
    return a * r * r

power(5, 64)
