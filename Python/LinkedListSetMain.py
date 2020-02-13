# coding=utf-8
from FileOperation import readFile
from BasicDS.LinkedListSet import LinkedListSet


if __name__ == "__main__":
    words1 = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words1))
    set1 = LinkedListSet()
    for item in words1:
        set1.add(item)
    print("Total different words: ", set1.getSize())

    print()

    words2 = readFile("./books/a-tale-of-two-cities.txt")
    print("a-tale-of-two-cities:")
    print("Total words: ", len(words2))
    set2 = LinkedListSet()
    for item in words2:
        set2.add(item)
    print("Total different words: ", set2.getSize())

