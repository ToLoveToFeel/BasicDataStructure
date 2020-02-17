# coding=utf-8
from BasicDS.MaxHeap import MaxHeap
from BasicDS.MinHeap import MinHeap


class PriorityQueue:

    def __init__(self, capacity=10, arr=None, isMaxHeap=True):
        if isMaxHeap:
            self.__data = MaxHeap(capacity=capacity, arr=arr)
        else:
            self.__data = MinHeap(capacity=capacity, arr=arr)

    # 获取队列大小
    def getSize(self):
        return self.__data.size()

    # 判断队列是否为空
    def isEmpty(self):
        return self.__data.isEmpty()

    # 入队
    def enqueue(self, e):
        self.__data.add(e)

    # 元素出队，同时返回队首元素
    def dequeue(self):
        return self.__data.extract()

    # 查看队首元素，不出队
    def getFront(self):
        return self.__data.find()

