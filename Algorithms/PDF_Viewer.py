#!/bin/python3

import sys

def designerPdfViewer(h, word):
    # Complete this function
    rect_base = len(word)
    rect_height = []
    ascii_a = ord('a')
    for i in range(0, len(word)):
        rect_height.append(h[(ord(word[i]))% ascii_a])
    return rect_base * max(rect_height)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result