import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    result = 0
    for i in range(0, n):
        result += ar[i]
    return result

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    print(str(result) + '\n')
