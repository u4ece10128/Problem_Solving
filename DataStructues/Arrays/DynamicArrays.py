#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    seq_list = []
    seq = []
    for i in range(n):
        seq_list.append(seq)

    for query in queries:
        print(query)
        index = (query[1] ^ lastAnswer) % n
        print(index)
        if query[0] == 1:
            seq_list[index].append(query[2])
        else:
            lastAnswer = query[2] % len(seq_list[index])
            print(lastAnswer)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
