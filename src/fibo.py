def fibo_rec(n):
    if n < 2:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_iter(n):
    results = [0, 1]
    for i in range(2, n + 1):
        results.append(results[-2] + results[-1])
    return results[-1]


def fibo_small(n):
    def f(a, b, n):
        if n == 1:
            return b
        return f(b, a + b, n - 1)
    if n == 0:
        return 0
    return f(0, 1, n)


def fibo_formula(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = 1 - phi
    return round((phi**n - psi**n) / 5**0.5)
