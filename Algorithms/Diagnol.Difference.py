def diagonalDifference(a):
    size_squarematrix = len(a[0])
    diag1_list = []
    diag2_list = []
    for i in range(0, size_squarematrix):
        diag1_list.append(a[i][i])
    for i in range(0, size_squarematrix):
        diag2_list.append(a[i][size_squarematrix - i - 1])

    return abs(sum(diag1_list) - sum(diag2_list))


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    print(str(result) + '\n')

