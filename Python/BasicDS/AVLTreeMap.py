# coding=utf-8
# @Time       : 2020/2/17
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : AVLTreeMap.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.AVLTree import AVLTree


class AVLTreeMap:
    """
    时间复杂度分析(平均)：n为元素个数
        增 add：O(logn)
        删 remove：O(logn)
        改 set：O(logn)
        查 get：O(logn)      contains：O(n)
    """
    def __init__(self):
        self.__avl = AVLTree()

    def getSize(self):
        return self.__avl.getSize()

    def isEmpty(self):
        return self.__avl.isEmpty()

    def add(self, key, value):
        self.__avl.add(key, value)

    def remove(self, key):
        self.__avl.remove(key)

    def set(self, key, value):
        self.__avl.set(key, value)

    def get(self, key):
        self.__avl.get(key)

    def contains(self, key):
        self.__avl.contains(key)

    def keySet(self):
        return self.__avl.keySet()

