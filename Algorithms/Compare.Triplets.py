import os
import sys

def solve(a0, a1, a2, b0, b1, b2):
    comparision_score_a = 0
    comparision_score_b = 0
    lst_1 = [a0, a1, a2]
    lst_2 = [b0, b1, b2]
    for i in range(0, len(lst_1)):
        if lst_1[i] > lst_2[i]:
            comparision_score_a += 1
        elif lst_1[i] == lst_2[i]:
            continue
        elif lst_1[i] < lst_2[i]:
            comparision_score_b += 1
    return [comparision_score_a, comparision_score_b]


if __name__ == '__main__':
    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    print(' '.join(map(str, result)))