from functools import lru_cache

fib_cache = {}


def fibonacci(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    return value


def fibonacci_memoized(n):
    # store key values in
    if n in fib_cache:
        return fib_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    fib_cache[n] = value
    return value


@lru_cache(maxsize=10000)
def fibonacci_memoized_builtin(n):

    return fibonacci(n)


if __name__ == "__main__":

    for i in range(1, 1000001):
        print(i, ": ", fibonacci_memoized_builtin(i))
