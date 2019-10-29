#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'getMaximumOutfits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY outfits
#  2. INTEGER money
#


def getMaximumOutfits(outfits, money):
    # Write your code here
    outfits.sort() #sorted
    number_outfits = 0
    if money >=  min(outfits):
        for gf in xrange(len(outfits)):
            if money != 0 and money >= outfits[gf]:
                number_outfits += 1
                money = money - outfits[gf]
            else:
                break
        return number_outfits
    else:
        return number_outfits


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    outfits_count = int(raw_input().strip())

    outfits = []

    for _ in xrange(outfits_count):
        outfits_item = int(raw_input().strip())
        outfits.append(outfits_item)

    money = int(raw_input().strip())

    result = getMaximumOutfits(outfits, money)

    # fptr.write(str(result) + '\n')

    # fptr.close()
