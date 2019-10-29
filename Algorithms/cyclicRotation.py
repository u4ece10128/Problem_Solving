def solution(A, K):
    # write your code in Python 3.6
    
    for i in range(K):
        new_arr = []
        last_elem = A[len(A)-1]
        del(A[len(A)-1])
        new_arr.append(last_elem)
        for ind in A:
            new_arr.append(ind)
        A = new_arr
    return A
    pass

A = [1, 2, 3, 4]
K = 2
solution(A, K)
