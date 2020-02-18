# coding=utf-8
# @Time       : 2020/2/13
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : BSTSet.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.BST import BST


class BSTSet:
    """
    时间复杂度分析(平均)：n为元素个数
    增 add：          O(logn)
    删 remove：       O(logn)
    查 contains：     O(logn)
    """
    def __init__(self):
        self.__bst = BST()

    def getSize(self):
        return self.__bst.getSize()

    def isEmpty(self):
        return self.__bst.isEmpty()

    def add(self, e):
        self.__bst.add(e)

    def contains(self, e):
        return self.__bst.contains(e)

    def remove(self, e):
        self.__bst.remove(e)


