# coding=utf-8
# @Time       : 2020/2/12
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : ArrayStack.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.Array import Array


class ArrayStack:
    """
    基本操作：
    getSize()：获取栈大小，O(1)
    isEmpty():判断栈是否为空，O(1)
    push()：入栈，O(1)
    pop()：元素出栈，同时返回栈顶元素，O(1)
    peek()：查看栈顶元素，不出栈，O(1)
    """
    def __init__(self, capacity=10):
        self.__arr = Array(capacity)

    # 获取栈大小
    def getSize(self):
        return self.__arr.getSize()

    # 判断栈是否为空
    def isEmpty(self):
        return self.__arr.isEmpty()

    # 入栈
    def push(self, e):
        self.__arr.addLast(e)

    # 元素出栈，同时返回栈顶元素
    def pop(self):
        return self.__arr.removeLast()

    # 查看栈顶元素，不出栈
    def peek(self):
        return self.__arr.getLast()

    def getCapacity(self):
        return self.__arr.getCapacity()

    def __str__(self):
        res = "ArrayStack: "
        res += "["
        for i in range(self.__arr.getSize()):
            res += str(self.__arr.get(i))
            if i != self.getSize() - 1:
                res += ", "
        res += "] top"
        return res
