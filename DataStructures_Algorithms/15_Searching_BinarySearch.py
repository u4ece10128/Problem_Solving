# Given a sorted list search for a target element optimally
# [1, 4, 6, 9, 12, 34, 45]
# Find 34


def binary_search(arr, target):
    """

    1. Find the middle element of the sorted list , if the middle num == target return target
    2. if not, check if the target value is one the less than the middle or greater the middle.
    3. Drop the sub list that does not expected to have the taraget value.
    4. Repeat the process until, target is found.
    5. if not found return 0
    :param arr: <list>
    :param target: <int>
    :return: <boolean>
    """
    first = 0
    last = len(arr) - 1
    found = False
    while not found and first <= last:
        middle = (first + last) // 2
        if arr[middle] == target:
            found = True
        else:
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found

if __name__ == "__main__":
    print(binary_search([1, 4, 6, 9, 12, 34, 45], 34))
