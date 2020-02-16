# coding=utf-8
import time
from FileOperation import *
from BasicDS.BSTSet import BSTSet
from BasicDS.Trie import Trie


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    
    startTime = time.time()
    print("pride-and-prejudice:")
    print("Total words: ", len(words))
    set = BSTSet()
    for word in words:
        set.add(word)
    for word in words:
        set.contains(word)
    print("Total different words: ", set.getSize())
    endTime = time.time()
    print("BSTSet : ", endTime - startTime, " s")

    print()

    startTime = time.time()
    print("pride-and-prejudice:")
    print("Total words: ", len(words))
    trie = Trie()
    for word in words:
        trie.add(word)
    for word in words:
        trie.contains(word)
    print("Total different words: ", trie.getSize())
    endTime = time.time()
    print("Trie : ", endTime - startTime, " s")

