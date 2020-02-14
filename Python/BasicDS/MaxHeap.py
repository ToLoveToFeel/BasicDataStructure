# coding=utf-8
from BasicDS.Array import Array


class MaxHeap:

    def __init__(self, capacity=10):
        self.__data = Array(capacity)

    # 返回堆中的元素个数
    def size(self):
        return self.__data.getSize()

    # 返回一个布尔值，表示堆中是否为空
    def isEmpty(self):
        return self.__data.isEmpty()

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    def __parent(self, index):
        if index == 0:
            raise Exception("index-0 doesn't have parent.")
        return int((index - 1) / 2)

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    def __leftChild(self, index):
        return index * 2 + 1

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    def __rightChild(self, index):
        return index * 2 + 2

    # 向堆中添加元素
    def add(self, e):
        self.__data.addLast(e)
        self.__siftUp(self.__data.getSize() - 1)

    def __siftUp(self, k):
        while k > 0 and self.__data.get(self.__parent(k)) < self.__data.get(k):  # TODO:最小堆更改此处
            self.__data.swap(self.__parent(k), k)
            k = self.__parent(k)

    # 看堆中的最大元素
    def findMax(self):
        if self.__data.getSize() == 0:
            raise Exception("Cannot findMax when heap is empty!")
        return self.__data.get(0)

    # 取出堆中最大元素
    def extractMax(self):
        ret = self.findMax()

        self.__data.swap(0, self.__data.getSize() - 1)
        self.__data.removeLast()
        self.__siftDown(0)

        return ret

    def __siftDown(self, k):
        while self.__leftChild(k) < self.__data.getSize():
            j = self.__leftChild(k)
            if (j + 1 < self.__data.getSize()) and (self.__data.get(j + 1) > self.__data.get(j)):
                j = self.__rightChild(k)
            # self.__data.get(j)是leftChild和rightChild中的最大值
            if self.__data.get(k) > self.__data.get(j):
                break

            self.__data.swap(j, k)
            k = j

    





