# coding=utf-8
import sys
import time
from FileOperation import readFile
from BasicDS.AVLTree import AVLTree
from BasicDS.BSTMap import BSTMap


if __name__ == "__main__":
    words = readFile("./books/pride-and-prejudice.txt")
    print("pride-and-prejudice:")
    print("Total words: ", len(words))
    # words = sorted(words[:5000])
    # sys.setrecursionlimit(10000)  # set the maximum depth as 150000

    startTime = time.time()
    bstMap = BSTMap()
    for word in words:
        if bstMap.contains(word):
            bstMap.set(word, bstMap.get(word) + 1)
        else:
            bstMap.add(word, 1)
    for word in words:
        bstMap.contains(word)
    endTime = time.time()
    print("BSTMap : ", endTime - startTime, " s")

    startTime = time.time()
    avl = AVLTree()
    for word in words:
        if avl.contains(word):
            avl.set(word, avl.get(word) + 1)
        else:
            avl.add(word, 1)
    for word in words:
        avl.contains(word)
    endTime = time.time()
    print("AVLTree : ", endTime - startTime, " s")

    # 测试AVL删除函数
    for word in words[:100]:
        avl.remove(word)
        if (not avl.isBST()) or (not avl.isBalanced()):
            raise Exception("error")



