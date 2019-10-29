import numpy as np


def mean(elems, number_of_elements):
    return np.around(sum(elems)/number_of_elements, decimals=1)


def median(elems, number_elems):
    sorted_array = np.sort(elems)
    if number_elems % 2 == 0:
        print(elems[number_elems/2])
        print(elems[(number_elems/2) + 1])
        return (elems[number_elems/2] + elems[(number_elems/2) + 1])/2
    else:
        return elems[int(number_elems/2)]


num_elements = int(raw_input())
arrays_elem = map(int, raw_input().rstrip().split())

array_numpy = np. array(arrays_elem)

print median(array_numpy.astype('float64'), num_elements)

