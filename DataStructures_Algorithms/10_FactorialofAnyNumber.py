# Find the factorial of a given number n


def factorial_iterative(n):
    """
    Calculates the factorial of a given number
    Complexity: O(N)
    :param n: <int>
    :return: <int>
    """
    result = 1
    for num in range(2, n+1):
        result *= num
    return result


def factorial_recursive(n):
    """
    Calculates the factorial of a given number using recursive approach
    Complexity: O(N)
    :param n: <int>
    :return: <int>
    """
    # base case
    # we keep going until we hit th base case
    if n == 2:
        return 2
    if n < 2:
        return 1

    return n * factorial_recursive(n-1)

if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_recursive(5))
