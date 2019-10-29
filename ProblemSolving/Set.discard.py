n = int(input())
set_a = set(int(x) for x in input().split(' '))
length_cmd = int(input())


def sumofset(inp_set):
    sum = 0
    for i in range(0, len(inp_set)):
        sum = sum + int(inp_set.pop())
    return sum


for i in range(0, length_cmd):
    c = input().split()
    if c[0] == 'pop':
        set_a.pop()
    if c[0] != 'pop':
        if int(c[1]) in set_a:
            if c[0] == 'discard':
                set_a.discard(int(c[1]))
            if c[0] == 'remove':
                set_a.remove(int(c[1]))
        else:
            continue

print(sumofset(set_a))

