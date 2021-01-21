# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def select_filling_station(tanks, demand, time):
    fill = -1
    max_wait = 9999
    for i in range(len(tanks)):
        if tanks[i][1] >= demand + tanks[i][0]:
            wait = max(tanks[i][0] - time, 0)
            if max_wait > wait:
                if wait == 0:
                    return 1
                else:
                    fill = i
                    max_wait = wait
    return fill


def solution(A, X, Y, Z):
    # write your code in Python 3.6
    tanks = [(0, X), (0, Y), (0, Z)]
    cur_time = 0

    for car_demand in A:
        station = select_filling_station(tanks, car_demand, cur_time)
        if station == -1:
            return -1
        if tanks[station][0] > cur_time:
            wait = tanks[station][0] - cur_time
            cur_time += wait
        tanks[station] = (tanks[station][0] + car_demand, tanks[station][1])
    return cur_time


if __name__ == "__main__":
    # input_list = [4, 10, 11, 12, 2, 1, 26, 3]
    input_list = [2, 8, 4, 3, 2]
    X, Y, Z = 7, 11, 3
    # input_list = "my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b"
    print(solution(input_list, X, Y, Z))
