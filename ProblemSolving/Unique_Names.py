# def unique_names(names1, names2):
#     for i in names2:
#         if i not in names1:
#             names1.append(i)
#     return names1
#
# names1 = ["Ava", "Emma", "Olivia"]
# names2 = ["Olivia", "Sophia", "Emma"]
# print(
#
#unique

# _names(names1, names2)) # should print Ava, Emma, Olivia, Sophia

n = int(input())

k = range(0, n)
v = range(n-1, -1, -1)

result= {}


for keys, values in zip(k, v):
    result[keys] = values


print result