# coding=utf-8
import time
from FileOperation import readFile
from BasicDS.HashSet import HashSet


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))

    startTime = time.time()
    hashSet = HashSet()
    for word in words:
        hashSet.add(word)
    for word in words:
        hashSet.contains(word)
    endTime = time.time()
    print("Total different words : ", hashSet.getSize())
    print("AVLTreeSet : ", endTime - startTime, " s")


