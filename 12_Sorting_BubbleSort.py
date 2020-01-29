# Given a list of un ordered array, implement bubble sorting algorithm
# [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def sort_by_bubble_sort(arr):
    """
    Given a list, return the sorted version pf the list using bubble sort
    Complexity: O(N^2)
    Space Complexity: O(1)
    :param arr: <list>
    :return: <list>
    """

    for outer in range(0, len(arr)):
        for inner in range(1, len(arr)):
            if arr[inner] < arr[inner-1]:
                temp = arr[inner-1]
                arr[inner-1] = arr[inner]
                arr[inner] = temp
    return arr
if __name__ == "__main__":
    print(sort_by_bubble_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
