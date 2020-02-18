# coding=utf-8
# @Time       : 2020/2/14
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : MinHeap.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.Array import Array


class MinHeap:

    def __init__(self, capacity=10, arr=None):
        if arr is not None:
            # 传入数组(list)，实现heapify
            self.__data = Array(arr=arr)
            for i in range(self.__parent(len(arr) - 1), -1, -1):
                self.__siftDown(i)
        else:
            self.__data = Array(capacity=capacity)

    # 返回堆中的元素个数
    def getSize(self):
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
        while k > 0 and self.__data.get(self.__parent(k)) > self.__data.get(k):
            self.__data.swap(self.__parent(k), k)
            k = self.__parent(k)

    # 看堆中的最小元素
    def findMin(self):
        if self.__data.getSize() == 0:
            raise Exception("Cannot findMin when heap is empty!")
        return self.__data.get(0)

    # 方便优先队列调用
    def find(self):
        return self.findMin()

    # 取出堆中最小元素
    def extractMin(self):
        ret = self.findMin()

        self.__data.swap(0, self.__data.getSize() - 1)
        self.__data.removeLast()
        self.__siftDown(0)

        return ret

    # 方便优先队列调用
    def extract(self):
        return self.extractMin()

    def __siftDown(self, k):
        while self.__leftChild(k) < self.__data.getSize():
            j = self.__leftChild(k)
            if (j + 1 < self.__data.getSize()) and (self.__data.get(j + 1) < self.__data.get(j)):
                j = self.__rightChild(k)
            # self.__data.get(j)是leftChild和rightChild中的最小值
            if self.__data.get(k) < self.__data.get(j):
                break

            self.__data.swap(j, k)
            k = j

    # 取出堆中的最小元素，并且替换成元素e
    def replace(self, e):
        ret = self.findMin()
        self.__data.set(0, e)
        self.__siftDown(0)
        return ret





