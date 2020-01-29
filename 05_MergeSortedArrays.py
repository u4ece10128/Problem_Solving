# Given Two  sorted arrays, implement a function returns the
# merged sorted arrays
# Example [0, 2, 3, 4] [0, 1, 5] --> [0, 0, 1, 2, 3, 4, 5]


def merge_arrays(arr1, arr2):
    """
    Function takes two sorted arrays as input
    :param arr1: List
    :param arr2: List
    :return: List
    """
    merged_array = []

    # if there is a n empty array as input return the non-empty array
    # as output
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    i = 0
    j = 0
    while ~(len(merged_array) == len(arr1) + len(arr2)):
        print(i, j)
        if i != len(arr1) and arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        if j != len(arr1) and arr1[i] < arr2[j]:
            merged_array.append(arr2[j])
            j += 1
    return merged_array

if __name__ == "__main__":
    print(merge_arrays([0, 1, 5, 7], [1, 2, 10]))
