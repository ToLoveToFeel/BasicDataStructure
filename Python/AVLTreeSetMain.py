# coding=utf-8
import time
from FileOperation import readFile
from BasicDS.AVLTreeSet import AVLTreeSet


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))

    startTime = time.time()
    avlSet = AVLTreeSet()
    for word in words:
        avlSet.add(word)
    for word in words:
        avlSet.contains(word)
    endTime = time.time()
    print("Total different words : ", avlSet.getSize())
    print("AVLTreeSet : ", endTime - startTime, " s")


