# coding=utf-8
import time
from FileOperation import readFile
from BasicDS.AVLTreeSet import AVLTreeSet


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))

    startTime = time.time()
    avlMap = AVLTreeSet()
    for word in words:
        avlMap.add(word)
    for word in words:
        avlMap.contains(word)
    endTime = time.time()
    print("AVLTreeSet : ", endTime - startTime, " s")


