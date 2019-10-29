#!/bin/python

from __future__ import print_function


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(0, len(grades)):
        rem = grades[i] % 5
        if rem >= 3 and grades[i] >= 38:
            grades[i] = grades[i] + (5 - rem)
        elif rem < 3 and grades[i] >= 38:
            grades[i] = grades[i]
        elif grades[i] < 38:
            grades[i] = grades[i]
    return grades




if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(grades)

    # f.write('\n'.join(map(str, result)))
    # f.write('\n')

    # f.close()

