# coding=utf-8
import time
from FileOperation import readFile
from BasicDS.AVLTreeMap import AVLTreeMap


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))

    startTime = time.time()
    avlMap = AVLTreeMap()
    for word in words:
        if avlMap.contains(word):
            avlMap.set(word, avlMap.get(word) + 1)
        else:
            avlMap.add(word, 1)
    for word in words:
        avlMap.contains(word)
    endTime = time.time()
    print("Total different words: ", avlMap.getSize())
    print("Frequency of pride: ", avlMap.get("pride"))
    print("Frequency of prejudice: ", avlMap.get("prejudice"))
    print("AVLTreeMap : ", endTime - startTime, " s")


