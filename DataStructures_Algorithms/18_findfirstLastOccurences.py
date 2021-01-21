def binary_search(arr, target):
    """

    """
    index = -1
    left = 0
    right = len(arr) - 1
    while left <= right :
        mid = (left + right) / 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
        
        if arr[mid] == target:
            return mid

    return index


if __name__ == "__main__":
    # input_list = [4, 10, 11, 12, 2, 1, 26, 3]
    input_list = [8,8,8,8,8]
    target = 8
    # input_list = [2, 2]
    print(binary_search(input_list, target))