def factorial(x):
    res = 1
    while x > 0:
        res *= x
        x -= 1
    return res
