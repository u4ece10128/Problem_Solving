# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # list --> dict
    check_num = 1
    A = sorted(A)
    for sorted_elem in A:
        if sorted_elem >= 0:
            check_num = sorted_elem + 1
        if check_num in A:
            continue
        else:
            return check_num


if __name__ == "__main__":
    # input_list = [4, 10, 11, 12, 2, 1, 26, 3]
    # input_list = [1, 3, 6, 4, 1, 2]
    input_list = [-1, -3]
    print(solution(input_list))
