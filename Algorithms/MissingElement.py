def solution(A):
    A.sort()
    N = len(A)
    if A[N-1] <= 0:
        return 1
    if A[0] < 1:
        return 1
    for i in range(N-1):
        print(i)
        if A[i] <= 0:
            if A[i + 1] > 1:
                return 1
            continue
        if A[i+1] - A[i] > 1:
            return A[i] + 1
    return A[N-1] + 1


A = [0]
print solution(A)