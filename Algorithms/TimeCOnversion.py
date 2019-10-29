import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    n = len(s)
    if s[n-2] == 'P':
        tmp = s.split(':')
        if tmp[0] != '12':
            tmp[0] = str(int(tmp[0]) + 12)
        if tmp[0] == '12':
            tmp[0] = tmp[0]
    if s[n - 2] == 'A':
        tmp = s.split(':')
        if tmp[0] == '12':
            tmp[0] = '00'
    s = ':'.join(tmp)
    return s[0:n-2]

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result + '\n')