# Given a list of positive whole numbers, find the pair that sums to a target value
# [4, 10, 11, 12, 2, 1, 26, 3] , target = 4
# if the target is not found return None


def find_matching_pair(lst, target):
    """
    The functions scans the entire list and loads it to a Hash table i.e dictionary. For every target-key, check if
    the complimented result exists in the hash table.
    Complexity : O(N)
    Space Complexity: O(N) , for creating a new hash table
    :param lst: <list>
    :param target: <int>
    :return: <list>
    """
    lst_to_hash = {}

    for element in lst:
        lst_to_hash[element] = True

    for element in lst:
        lst_to_hash.pop(element, None)
        if target - element in lst_to_hash:
            return [element, target - element]
    return None


if __name__ == "__main__":
    # input_list = [4, 10, 11, 12, 2, 1, 26, 3]
    input_list = [14, 13, 6, 7, 8, 10, 1, 2]
    # input_list = [2, 2]
    print(find_matching_pair(input_list, 3))
