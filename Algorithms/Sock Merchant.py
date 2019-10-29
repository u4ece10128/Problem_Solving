#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    done = False
    not_to_visit = []
    i = 0
    j = i + 1
    num_pairs = 0
    while(~done):
        print('enter')
        if i < n - 1:
            if (i not in not_to_visit) and (ar[i] == ar[j]):
                num_pairs += 1
                not_to_visit.append(j)
                i = i + 1
                j = i + 1
            else:
                j += 1
        elif i > n - 1 :
            done = True
    return num_pairs


if __name__ == '__main__':

    n = int(input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    print result

