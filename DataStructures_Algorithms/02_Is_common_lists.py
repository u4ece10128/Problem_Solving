# Given two lists, return true or false if the lists have the common element
# Example : arr1 = ['a', 'b', 'c']
#           arr2 = ['s', 'g']
#           return False
# Example:  arr1 = ['a', 'b', 'c']
#           arr2 = ['s', 'g', 'f', 'b']
#           return True

# brute force approach


def is_common_element(arr1, arr2):
    """
    Loop through Array 1 and simultaneously search in the array 2 
    Time Complexity : O(N**2)
    :param arr1: List
    :param arr2: List
    :return: Boolean
    """
    for i in arr1:
        for j in arr2:
            if i == j:
                return True

    return False

# Optimal Approach


def is_common_element_optim(arr1, arr2):
    """
    Create a dictionary with lists elements as keys and loop through the second array
    check if the second array exists in the keys
    :param arr1: List
    :param arr2: List
    :return: Boolean
    """
    dict_arr1 = {}

    for i in range(0, len(arr1)):
        if arr1[i] not in dict_arr1.keys():
            dict_arr1[arr1[i]] = True
    print(dict_arr1)

    for i in range(0, len(arr2)):
        if arr2[i] in dict_arr1.keys():
            return True
    return False

if __name__ == "__main__":
    a = ['a', 'b', 'g']
    b = ['f', 'c', 'f', 'e']

    print(is_common_element(a, b))
    print(is_common_element_optim(a, b))
