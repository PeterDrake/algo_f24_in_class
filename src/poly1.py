def poly(x, coefficients):
    result, i = 0, 0
    for n in coefficients:
        result += n * x ** i
        i += 1
    return result


def horner(x, coefficients):
    if not coefficients:
        return 0
    return coefficients[0] + x * horner(x, coefficients[1:])
