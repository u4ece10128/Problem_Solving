n = int(input())
rollnum_1 = set(int(x) for x in input().split(' '))
m = int(input())
rollnum_2 = set(int(x) for x in input().split(' '))

print(len(rollnum_1.intersection(rollnum_2)))