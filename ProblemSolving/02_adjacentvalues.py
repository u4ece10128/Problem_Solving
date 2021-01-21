# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # covert list to dict to keep track of number of occurenrece of every 
    # element
    if len(A) != 0:
        from collections import defaultdict
        elem_map = defaultdict(int)
        for elem in A:
            elem_map[elem] += 1
            if elem_map[elem] > 1:
                # if there are more than one ocurnece of an element
                # then those are the adjacent values with abs diff zero
                return 0
        # sort the array
        # Complexity: NlogN
        A = sorted(A)
        # at this point every element in A occurs only once
        # the sorted makes sure that values are asceneding order
        # scan the array to calculate the adjacent values difference
        result = []
        for i in range(0, len(A) - 1):
            result.append(abs(A[i] - A[i+1]))
        if min(result) > 100000000:
            return -1
        return min(result)
    else:
        return -2


if __name__ == "__main__":
    # input_list = [4, 10, 11, 12, 2, 1, 26, 3]
    input_list = [0, 6, 7, 5, 3, 11, 2]
    # input_list = "my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b"
    print(solution(input_list))