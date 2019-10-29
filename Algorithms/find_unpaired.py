
def solution(A):
    # write your code in Python 3.6
    unpaired = 0
    for i in range(len(A)):
        if len(A) == 1:
            unpaired = A[0]
            break
        unpaired = unpaired ^ A[i]

    return unpaired

A = [42]
print((solution(A)))