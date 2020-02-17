# coding=utf-8
from FileOperation import readFile
from BasicDS.AVLTree import AVLTree


if __name__ == "__main__":
    words1 = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words1))
    map = AVLTree()
    for word in words1:
        if map.contains(word):
            map.set(word, map.get(word) + 1)
        else:
            map.add(word, 1)
    print("Total different words: ", map.getSize())
    print("Frequency of PRIDE: ", map.get("pride"))
    print("Frequency of PREJUDICE: ", map.get("prejudice"))
    print("is BST : ", map.isBST())
    print("is Balanced : ", map.isBalanced())


