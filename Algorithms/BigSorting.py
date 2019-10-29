#!/bin/python

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    temp =[]
    for _ in xrange(len(unsorted)):
        t = min(unsorted)
        print t
        temp.append(str(t))
        unsorted.remove(t)
    return temp

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    unsorted = []
# xrange() takes less memory when compared to range()
    for _ in xrange(n):
        unsorted_item = int(raw_input())
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()