def poly(a, coefficients):
    total = 0
    factor = 1
    for c in coefficients:
        total += c * factor
        factor *= a
    return total


def horner(x, coefficients):
    if not coefficients:
        return 0
    return coefficients[0] + x * horner(x, coefficients[1:])
