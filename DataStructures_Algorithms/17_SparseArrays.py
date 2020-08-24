

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    strings_dict ={}
    for key in strings:
        if key not in strings_dict:
            strings_dict[key] = 1
        else:
            strings_dict[key] += 1
    instances = []
    for query in queries:
        if query in strings_dict:
            instances.append(strings_dict[query])
        else:
            instances.append(0)
    return instances


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print(res)
    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
