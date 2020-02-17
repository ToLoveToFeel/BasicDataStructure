# coding=utf-8
import time
from FileOperation import *
from BasicDS.HashTable import HashTable


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))

    startTime = time.time()
    ht = HashTable(131071)
    for word in words:
        if ht.contains(word):
            ht.set(word, ht.get(word) + 1)
        else:
            ht.add(word, 1)
    for word in words:
        ht.contains(word)
    endTime = time.time()
    print("BSTMap : ", endTime - startTime, " s")

