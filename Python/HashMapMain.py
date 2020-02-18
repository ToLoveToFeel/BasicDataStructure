# coding=utf-8
import time
from FileOperation import readFile
from BasicDS.HashMap import HashMap


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))

    startTime = time.time()

    hashMap = HashMap()
    for word in words:
        if hashMap.contains(word):
            hashMap.set(word, hashMap.get(word) + 1)
        else:
            hashMap.add(word, 1)
    for word in words:
        hashMap.contains(word)

    endTime = time.time()

    print("Total different words: ", hashMap.getSize())
    print("Frequency of pride: ", hashMap.get("pride"))
    print("Frequency of prejudice: ", hashMap.get("prejudice"))
    print("AVLTreeMap : ", endTime - startTime, " s")




