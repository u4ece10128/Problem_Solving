from collections import OrderedDict


def happinesscore(number, input_array, array1, array2):
    happiness_score = 0
    for i in range(0, int(number)):
        if input_array[i] in array1:
            happiness_score = happiness_score + 1
        elif input_array[i] in array2:
            happiness_score = happiness_score - 1
        elif input_array[i] not in array1 or array2:
            happiness_score = happiness_score

    return happiness_score


[n, m] = input().split()
int_array = input().split()
#Start: removing duplicates
int_array = list(OrderedDict.fromkeys(int_array))
#End: Removing Duplicates
A_arr = set(input().split(' '))
B_arr = set(input().split(' '))
Score = happinesscore(n, int_array, A_arr, B_arr)
print(Score)
