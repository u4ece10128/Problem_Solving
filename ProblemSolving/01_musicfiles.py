# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    extensions_map = {
        'mp3': 'music',
        'aac': 'music',
        'flac': 'music',
        'jpg': 'images',
        'bmp': 'images',
        'gif': 'images',
        'mp4': 'movies',
        'avi': 'movies',
        'mkv': 'movies'
    }
    S = S.split('b')[:-1]
    files_map = {'music': 0, 'images': 0, 'movies': 0, 'other': 0}
    for item in S:
        tmp = item.rsplit('.', 1)[1].split(' ')
        if tmp[0] in extensions_map:
            key_to_dict = extensions_map[tmp[0]]
            files_map[key_to_dict] += int(tmp[1])
        else:
            files_map['other'] += int(tmp[1])
    tmp = str()
    for index, tup in enumerate(files_map.items()):
        if index == len(files_map) - 1:
            tmp += f'{tup[0]} {tup[1]}b'
        else:
            tmp += f'{tup[0]} {tup[1]}b\n'
    return tmp


if __name__ == "__main__":
    # input_list = [4, 10, 11, 12, 2, 1, 26, 3]
    # input_list = [1, 3, 6, 4, 1, 2]
    input_list = "my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b"
    print(solution(input_list))
