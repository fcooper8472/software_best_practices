# Fergus's favourite functions


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def is_perfect_number(n):

    if n < 0:
        raise ValueError("The number %s is negative!" % n)

    if n in [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]:
        return true
    return false
