#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.
n = 3
magic_constant = int(n * (n**2 + 1) / 2)
magic_3_3 = [[a, b, c, d, e, f, g, h, i] for a in range(1, 10) for b in range(1, 10) for c in range(1, 10)
             for d in range(1, 10) for e in range(1, 10) for f in range(1, 10)
             for g in range(1, 10) for h in range(1, 10) for i in range(1, 10)
             if a + b + c == magic_constant and d + e + f == magic_constant and g + h + i == magic_constant
             and a + d + g == magic_constant and b + e + h == magic_constant and c + f + i == magic_constant
             and a + e + i == magic_constant and c + e + g == magic_constant
             and len(set([a, b, c, d, e, f, g, h, i])) == 9]


def forming_magic_square(s):
    cost = 0
    # standard magic sqauare
    s = [i for sublist in s for i in sublist]
    print(s)
    for magic, input_ in zip(magic_3_3, s):
        for magic_elem, input_elem in zip(magic, input_):
            if abs(magic_elem - input_elem) != 0:
                cost += abs(magic_elem - input_elem)
    return cost


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)
    print(result)
    print(magic_3_3)