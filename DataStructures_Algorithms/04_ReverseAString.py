# Give a string of length N, implement a function that revereses the string
# Example: "My name is Jaya Ram"  --? "maR si eman yM"


def reverse_string(s):
    """
    Function takes in a string and returns the reversed form of the same
    Time Complexity: O(N)
    :param s: str
    :return: str
    """
    str_lst = [c for c in s]  # O(N)
    reverse_str = ''
    for i in range(len(str_lst)-1, -1, -1):  # O(N)
        reverse_str += str_lst[i]
    return reverse_str


def reverse_string_recursive(s):
    # base case
    if len(s) < 2:
        return s
    return reverse_string_recursive(s[1:]) + s[0]

if __name__ == "__main__":
    sample_str = "My name is Jaya Ram"
    print(reverse_string(sample_str))
    print(reverse_string_recursive(sample_str))
