# Complete the staircase function below.


def staircase(n):
    for i in range(1, n + 1):
        target_str = []
        allign_spaces = []
        for k in range (0, n - i):
            allign_spaces.append(' ')
        for j in range(0, i):
            target_str.append('#')
        target = ''.join(allign_spaces) + ''.join(target_str)
        print target

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)

