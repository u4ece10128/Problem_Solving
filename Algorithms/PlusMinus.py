#!/bin/python

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    num_pos = 0
    num_neg = 0
    num_zeros = 0
    l = len(arr)
    for i in range(0, l):
        if arr[i] > 0:
            num_pos = num_pos + 1
        elif arr[i] == 0:
            num_zeros += 1
        elif arr[i] < 0:
            num_neg +=1
    return float(num_pos)/float(l), float(num_zeros)/float(l), float(num_neg)/float(l)

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    [pos, zero, neg] = plusMinus(arr)
    print '%.6f' % pos
    print '%.6f' % neg
    print '%.6f' % zero


