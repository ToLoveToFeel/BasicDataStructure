# coding=utf-8
# @Time       : 2020/2/12
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : LoopQueue.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


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
    def __init__(self, capacity=10):
        self.__data = [0 for _ in range(capacity + 1)]
        self.__front = 0  # 队首
        self.__tail = 0  # 队尾
        self.__size = 0  # 循环队列实际大小

    # 获取队列大小
    def getSize(self):
        return self.__size

    # 判断队列是否为空
    def isEmpty(self):
        return self.__front == self.__tail

    # 入队
    def enqueue(self, e):
        if (self.__tail + 1) % len(self.__data) == self.__front:
            self.__resize(self.getCapacity() * 2)
        self.__data[self.__tail] = e
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__size += 1

    # 元素出队，同时返回队首元素
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue from an empty queue.")

        ret = self.__data[self.__front]
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        if (self.__size == int(len(self.__data) / 4)) and (int(len(self.__data) / 2) != 0):  # 缩容，Lazy，防止复杂度震荡
            self.__resize(int(len(self.__data) / 2))
        return ret

    # 查看队首元素，不出队
    def getFront(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        return self.__data[self.__front]

    def getCapacity(self):
        return len(self.__data) - 1

    def __resize(self, newCapacity):
        newData = [0 for _ in range(newCapacity + 1)]
        for i in range(self.__size):
            newData[i] = self.__data[(i + self.__front) % len(self.__data)]
        del self.__data
        self.__data = newData
        self.__front = 0
        self.__tail = self.__size

    # 用户调用print(u)输出的字符串形式，u为该类的对象
    def __str__(self):
        res = "LoopQueue: size = {0} , capacity = {1}\n".format(self.__size, self.getCapacity())
        res += "front ["

        i = self.__front
        while i != self.__tail:
            res += str(self.__data[i])
            if (i + 1) % len(self.__data) != self.__tail:
                res += ", "
            i = (i + 1) % len(self.__data)

        res += "] tail"
        return res
