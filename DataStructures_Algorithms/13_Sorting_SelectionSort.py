# Given an unsorted list, return the sorted list by using selection sort
# [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def sort_by_selection(arr):
    """
     Given a list, return the sorted version pf the list using selection sort,
     Scans for the shortest element in the list and swaps with the starting point of the scanning
    :param arr:
    :return:
    """
    for outer in range(0, len(arr)):
        temp, current_min_index = arr[outer], outer
        for inner in range(outer+1, len(arr)):
            if arr[inner] < arr[current_min_index]:
                current_min_index = inner
        arr[outer] = arr[current_min_index]
        arr[current_min_index] = temp
    return arr
if __name__ == "__main__":
    print(sort_by_selection([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
