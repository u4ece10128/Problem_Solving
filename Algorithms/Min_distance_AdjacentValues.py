def min_distance(arr, num1, num2):
    nPos1 = len(arr)
    nPos2 = len(arr)
    for i in range(len(arr)):
        if(arr[i] == num1):
            nPos1 = i
        if(arr[i] == num2):
            nPos2 = i
        print(nPos1)
        if nPos1 < len(arr) and nPos2 < len(arr):
            min_distance = abs(nPos1 - nPos2)
            elems = range(arr[nPos1], arr[nPos2], 1)
            for j in elems:
                if j not in arr:
                    adjacent = True
                else:
                    adjacent = False
            if adjacent:
                if min_distance > 100000000:
                    return -1
                else:
                    return min_distance
            if ~adjacent:
                return -2


def solution(A):
    A.sort()
    return min_distance(A, 3, 3)


A = [0, 3, 3, 7, 5, 3, 11, 1]
print(solution(A))