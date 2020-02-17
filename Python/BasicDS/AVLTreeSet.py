# coding=utf-8
# @Time       : 2020/2/17
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : AVLTreeSet.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.AVLTree import AVLTree


class AVLTreeSet:
    """
    时间复杂度分析(平均)：n为元素个数
        增 add：          O(logn)
        删 remove：       O(logn)
        查 contains：     O(logn)
    """
    def __init__(self):
        self.__avl = AVLTree()

    def getSize(self):
        return self.__avl.getSize()

    def isEmpty(self):
        return self.__avl.isEmpty()

    def add(self, e):
        if not self.__avl.contains(e):
            self.__avl.add(e, None)

    def contains(self, e):
        self.__avl.contains(e)

    def remove(self, e):
        self.__avl.remove(e)

