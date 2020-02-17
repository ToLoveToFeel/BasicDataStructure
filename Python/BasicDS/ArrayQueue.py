# coding=utf-8
# @Time       : 2020/2/12
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : ArrayQueue.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.Array import Array


class ArrayQueue:
    """
    基本操作：
    getSize()：获取队列大小，O(1)
    isEmpty():判断队列是否为空，O(1)
    enqueue()：入队，O(1)
    dequeue()：元素出队，同时返回队首元素，O(n)
    getFront()：查看队首元素，不出队，O(1)
    """
    def __init__(self, capacity=10):
        self.__arr = Array(capacity)

    # 获取队列大小
    def getSize(self):
        return self.__arr.getSize()

    # 判断队列是否为空
    def isEmpty(self):
        return self.__arr.isEmpty()

    # 入队
    def enqueue(self, e):
        self.__arr.addLast(e)

    # 元素出队，同时返回队首元素
    def dequeue(self):
        return self.__arr.removeFirst()

    # 查看队首元素，不出队
    def getFront(self):
        return self.__arr.getFirst()

    def getCapacity(self):
        return self.__arr.getCapacity()

    def __str__(self):
        res = "ArrayQueue: "
        res += "front ["
        for i in range(self.__arr.getSize()):
            res += str(self.__arr.get(i))
            if i != self.getSize() - 1:
                res += ", "
        res += "] tail"
        return res
