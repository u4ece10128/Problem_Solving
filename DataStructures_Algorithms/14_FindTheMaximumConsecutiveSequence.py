# Given a list of numbers, find the maximum length of the consecutive sequence
# A = [5, 2, 1, 99, 1, 4, 3, 100]
# Result: [[1,2,3,4,5], [99, 100]] --> 5


def find_max_consecutive_sequence(arr):
    """
    Finds the maximum length of the consequtive sequence
    1. Transform list to Hash set , python duct --> O(N)
    2. Look for every key in the dict, if not visited, look for if there exists key - 1 and key + 1
    and append it to a list
    3. Repeat the process until all the keys are visited
    :param arr: <list>
    :return: <int>
    """
    hash_set = {}
    visited_elem = []
    length = 0
    result = 0
    for i in arr:
        if i not in hash_set:
            hash_set[i] = True

    for key in hash_set:
        if key not in visited_elem:
            visited_elem.append(key)
            length += 1
            forward = key + 1
            while forward in hash_set:
                visited_elem.append(forward)
                forward += 1
                length += 1

            backward = key - 1
            while backward in hash_set:
                visited_elem.append(backward)
                backward -= 1
                length += 1
            result = max(result, length)
            length = 0
    return result

if __name__ == "__main__":
    print(find_max_consecutive_sequence([5, 2, 1, 99, 1, 4, 3, 100]))
