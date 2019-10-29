
def solution(N):
    source_number = str(N)
    res = []
    counter = len(source_number)
    while counter != 0:
        res.append(max(source_number))
        source_number = source_number.replace(max(source_number), '', 1)
        counter -= 1
    return int(''.join(res))


N = 909
result = (solution(N))
print result