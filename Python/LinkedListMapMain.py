# coding=utf-8
from FileOperation import readFile
from BasicDS.LinkedListMap import LinkedListMap


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))
    map = LinkedListMap()
    for word in words:
        if map.contains(word):
            map.set(word, map.get(word) + 1)
        else:
            map.add(word, 1)
    print("Total different words: ", map.getSize())
    print("Frequency of PRIDE: ", map.get("pride"))
    print("Frequency of PREJUDICE: ", map.get("prejudice"))


