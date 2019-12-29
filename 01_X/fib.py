# f(n) = f(n-1) + f(n-2)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    assert(n >= 0)
    a, b = 0, 1
    for i in range(1, n + 1):
        a, b = b, a + b
    return a


print(fib2(352))
