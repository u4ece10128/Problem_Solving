# Given a number N return the index value of the fibonacci sequence, where the sequence is
# 0, 1, 1, 2, 3, 5, 8, 31, 21....
# the pattern of the sequence is that each value is the sum of the previous two values


def fibonacci_iterative(n):
    """
    Genrates a fibonacci of n
    Complexity: O(N)
    :param n: <int>
    :return: <int>
    """
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i - 2])
    return arr[n]


def fibonacci_recursive(n):
    """
    Returns the index of the fibonacci number
    Complexity: O(2^N) , we can make thi sbetter by using dynamic programming or memoization
    :param n: <int>
    :return: <int>
    """
    # base case
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == "__main__":
    print(fibonacci_iterative(3))
