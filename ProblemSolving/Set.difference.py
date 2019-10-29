n = int(input())
rollnum_1 = set(int(x) for x in input().split(' '))
m = int(input())
rollnum_2 = set(int(x) for x in input().split(' '))

print(len(rollnum_1.difference(rollnum_2)))

#Symmetric diff -- in a or B but not in both

n = int(input())
rollnum_1 = set(int(x) for x in input().split(' '))
m = int(input())
rollnum_2 = set(int(x) for x in input().split(' '))

print(len(rollnum_1.symmetric_difference(rollnum_2)))