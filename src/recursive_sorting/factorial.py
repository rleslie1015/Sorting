# $! = 4 * 3 * 2 * 1 = 24

def factorial(n):
    # Return the product of n and every positive integer below
    # Assume that n is a positive integer >= 1
    if n == 1:
        return 1
    elif n == 2:
        return 2 * 1
    elif n == 3:
        return 3 * 2 * 1
    elif n == 4:
        return 4 * 3 * 1
    elif n == 5:
        return 5 * 4 * 3 * 2 * 1


def fib(n):
    # return the nth number in the fibonacci sequence
    # the next number is found by adding up the two prevous numbers
    print(f"calculating fib({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2) 