# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let  be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:
# Ensure rows x columns >= L
import math as mt


def encrypt(text):
    """
    Complexity: O(N**2)
    :param text:
    :return:
    """
    text = text.replace(" ", "")
    l = len(text)

    row, col = mt.floor(mt.sqrt(l)), mt.ceil(mt.sqrt(l))
    # row is always less than or equal to col
    while row * col < l:
        row += 1
    result = []
    for j in range(col):
        temp = []
        for i in range(j, l, col):
            temp.append(text[i])
        result.append(''.join(temp))
    return ' '.join(result)


if __name__ == "__main__":
    print(encrypt(input()))
