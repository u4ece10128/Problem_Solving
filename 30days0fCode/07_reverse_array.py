if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rev_arr = list()

    for i in range(n - 1, -1, -1):
        rev_arr.append(arr[i])
    print(*rev_arr)
