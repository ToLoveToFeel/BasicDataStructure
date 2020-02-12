# coding=utf-8
from BasicDS.Arrays import Array


class ArrayQueue:
    """
    基本操作：
    getSize()：获取队列大小，O(1)
    isEmpty():判断队列是否为空，O(1)
    enqueue()：入队，O(1)
    dequeue()：元素出队，同时返回队首元素，O(n)
    getFront()：查看队首元素，不出队，O(1)
    """
    def __init__(self, capacity=10, dtype="int"):
        self.arr = Array(capacity, dtype)

    # 获取队列大小
    def getSize(self):
        return self.arr.getSize()

    # 判断队列是否为空
    def isEmpty(self):
        return self.arr.isEmpty()

    # 入队
    def enqueue(self, e):
        self.arr.addLast(e)

    # 元素出队，同时返回队首元素
    def dequeue(self):
        return self.arr.removeFirst()

    # 查看队首元素，不出队
    def getFront(self):
        return self.arr.getFirst()

    def getCapacity(self):
        return self.arr.getCapacity()

    def __str__(self):
        res = "ArrayQueue: "
        res += "front ["
        for i in range(self.arr.getSize()):
            res += str(self.arr.get(i))
            if i != self.getSize() - 1:
                res += ", "
        res += "] tail"
        return res
