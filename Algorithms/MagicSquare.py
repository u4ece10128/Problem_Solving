def formingMagicSquare(s):
    size_squarematrix = len(s[0])
    tmp = [[0 for x in range(size_squarematrix)] for y in range(size_squarematrix)]
    cost = []
    cnt = []
    check = set()
    arm = 0
    magic_score = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    for m in range(1, 10):
                        tmp[0][0] = i
                        tmp[0][1] = j
                        tmp[0][2] = k
                        tmp[1][0] = l
                        tmp[1][1] = m
                        magic_constant = tmp[0][0] + tmp[0][1] + tmp[0][2]
                        tmp[1][2] = magic_constant - tmp[1][0] - tmp[1][1]
                        tmp[2][0] = magic_constant - tmp[0][0] - tmp[1][0]
                        tmp[2][1] = magic_constant - tmp[0][1] - tmp[1][1]
                        tmp[2][2] = magic_constant - tmp[0][2] - tmp[1][2]
                        # one random matrix is generated
                        # checking repeated elements in the matrix
                        for c in range(0, size_squarematrix):
                            for d in range(0, size_squarematrix):
                                check.add(tmp[c][d])
                        for mj in check:
                            if mj < 0 or mj > 9:
                                    arm += 1
                            else:
                                continue
                        row1 = sum(tmp[:][0])
                        row2 = sum(tmp[:][1])
                        row3 = sum(tmp[:][2])
                        col1 = sum(tmp[0][:])
                        col2 = sum(tmp[1][:])
                        col3 = sum(tmp[2][:])
                        diag1 = tmp[0][0] + tmp[1][1] + tmp[2][2]
                        diag2 = tmp[0][2] + tmp[1][1] + tmp[2][0]
                        if row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == 15:
                            magic_score += 1
                        if len(check) == 9 and arm == 0 and magic_score == 1:
                            for a in range(0, size_squarematrix):
                                for b in range(0, size_squarematrix):
                                    replacement_value = abs(tmp[a][b] - s[a][b])
                                    cnt.append(replacement_value)
                            cost.append(sum(cnt))
                            check = set()
                        check = set()
                        arm = 0
                        magic_score = 0
                        replacement_value = 0
                        cnt = []

    return min(cost)


if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
