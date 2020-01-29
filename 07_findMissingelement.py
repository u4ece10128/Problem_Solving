# Given two lists find the missing element
# full_list = [4, 9, 12, 5, 6]
# partial list = [4, 12, 9, 6]
# Result: 5


def find_missing(full_list, partial_list):
    """
    Function finds the missing element from the partial list by scanning the full list
    Complexity: O(N) , list lookup --> O(1)
    Space Complexity: O(1) , we only create one integer variable
    :param full_list: <list>
    :param partial_list: <list>
    :return: <int>
    """
    for i in full_list:
        if i not in partial_list:
            return i


def find_missing_use_xor(full_list, partial_list):
    """
    XOR Between same elements gives zero, if we xor the entire elements in both lists, the same element results in zero,
    leaving out the missing element
    Complexity: O(N)
    Space Complexity : O(1)
    :param full_list: <list>
    :param partial_list: <list>
    :return: <int>
    """
    xor_sum = 0
    for x in full_list:
        xor_sum ^= x
    for y in partial_list:
        xor_sum ^= y
    return xor_sum

if __name__ == "__main__":
    full = [4, 9, 12, 5, 6]
    partial = [4, 12, 9, 6]
    print("The Missing element is {}".format(find_missing_use_xor(full, partial)))
