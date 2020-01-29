# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return None

# naive solution


def find_first_recurring_character_naive(arr):
    """
    Complexity O(N^2)
    :param arr:
    :return:
    """
    index_characters = []
    nearest = -100
    for i in range(0, len(arr)):
        for j in (i+1, len(arr)):
            if arr[i] == arr[j]:
                # found first recurring character
                index_characters.append(j)
        nearest = min(index_characters)


def find_first_recurring_character(arr):
    """
    Function that implements, finding the first recurring character
    Complexity: O(N)
    We are using Hash tables to store the data type integer
    :param arr:
    :return:
    """
    map_dict = {}

    for i in range(0, len(arr)):
        if arr[i] in map_dict:
            return arr[i]
        else:
            map_dict[arr[i]] = i
    return None
if __name__ == "__main__":
    arr1 = [2, 5, 1,  3, 4]
    print(find_first_recurring_character(arr1))

