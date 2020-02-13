# coding=utf-8
from BasicDS.BST import BST


class BSTSet:
    def __init__(self):
        self.__bst = BST()

    def getSize(self):
        return self.__bst.getSize()

    def isEmpty(self):
        return self.__bst.isEmpty()

    def add(self, e):
        self.__bst.add(e)

    def contains(self, e):
        self.__bst.contains(e)

    def remove(self, e):
        self.__bst.remove(e)


