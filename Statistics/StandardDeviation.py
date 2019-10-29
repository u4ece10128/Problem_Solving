
n = int(input())
X = [int(x) for x in input().split()]

mean = sum(X) / n
variance = sum([((x - mean) ** 2) for x in X]) / n
stddev = variance ** 0.5

print("{0:0.1f}".format(stddev))
