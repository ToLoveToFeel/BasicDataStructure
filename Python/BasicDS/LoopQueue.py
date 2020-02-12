# coding=utf-8
import numpy as np


class LoopQueue:
    """
    队列为空：front == tail
             front
            |    |    |    |    |    |    |    |  capacity
             tail
    队列满：(tail + 1) % c == front
                       front
            | 11 |    | 33 | 44 | 55 | 66 | 77 |  capacity
                  tail
    基本操作：
    getSize()：获取队列大小，O(1)
    isEmpty():判断队列是否为空，O(1)
    enqueue()：入队，O(1)，均摊
    dequeue()：元素出队，同时返回队首元素，O(1)，均摊
    getFront()：查看队首元素，不出队，O(1)
    """
    # 构造函数
    def __init__(self, capacity=10, dtype="int"):
        self._data = np.zeros(shape=capacity+1, dtype=eval(dtype))
        self._front = 0  # 队首
        self._tail = 0  # 队尾
        self._size = 0  # 循环队列实际大小
        self._dtype = dtype

    # 获取队列大小
    def getSize(self):
        return self._size

    # 判断队列是否为空
    def isEmpty(self):
        return self._front == self._tail

    # 入队
    def enqueue(self, e):
        if (self._tail + 1) % len(self._data) == self._front:
            self.__resize(self.getCapacity() * 2)
        self._data[self._tail] = e
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    # 元素出队，同时返回队首元素
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        ret = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if (self._size == int(len(self._data) / 4)) and (int(len(self._data) / 2) != 0):  # 缩容，Lazy，防止复杂度震荡
            self.__resize(int(len(self._data) / 2))
        return ret

    # 查看队首元素，不出队
    def getFront(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        return self._data[self._front]

    def getCapacity(self):
        return len(self._data) - 1

    def __resize(self, newCapacity):
        newData = np.zeros(shape=newCapacity+1, dtype=eval(self._dtype))
        for i in range(self._size):
            newData[i] = self._data[(i + self._front) % len(self._data)]
        del (self._data)
        self._data = newData
        self._front = 0
        self._tail = self._size

    # 用户调用print(u)输出的字符串形式，u为该类的对象
    def __str__(self):
        res = "LoopQueue: size = {0} , capacity = {1}\n".format(self._size, self.getCapacity())
        res += "front ["

        i = self._front
        while i != self._tail:
            res += str(self._data[i])
            if (i + 1) % len(self._data) != self._tail:
                res += ", "
            i = (i + 1) % len(self._data)

        res += "] tail"
        return res
