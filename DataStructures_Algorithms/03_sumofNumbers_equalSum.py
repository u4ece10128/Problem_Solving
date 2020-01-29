# google interview Question, given a collection of numbers , find the pair of
# numbers that add upto given sum
# Example: [1, 2, 3, 9] , sum = 8 ;; return False
# Example: [1, 2, 4, 4] , sum = 8 ;; return True


def findmathchingpair(arr1, objective_sum):
    """
    Given a sorted array, the function returns True if found a pair that adds upto given sum
    Time Complexity: O(N)
    :param arr1: List
    :param objective_sum: int
    :return: Boolean
    """
    left_id, right_id = 0, len(arr1) - 1
    while left_id != right_id:
        res = arr1[left_id] + arr1[right_id]
        if res == objective_sum:
            return True
        if res > objective_sum:
            right_id -= 1
        if res < objective_sum:
            left_id += 1
    return False

if __name__ == "__main__":
    a = [1, 2, 4, 4]
    print(findmathchingpair(a, 2))
