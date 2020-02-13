# coding=utf-8
from BasicDS.LinkedList import LinkedList


class LinkedListStack:
    """
    基本操作：
    getSize()：获取栈大小，O(1)
    isEmpty():判断栈是否为空，O(1)
    push()：入栈，O(1)
    pop()：元素出栈，同时返回栈顶元素，O(1)
    peek()：查看栈顶元素，不出栈，O(1)
    """
    def __init__(self):
        self._list = LinkedList()

    # 获取栈大小
    def getSize(self):
        return self._list.getSize()

    # 判断栈是否为空
    def isEmpty(self):
        return self._list.isEmpty()

    # 入栈
    def push(self, e):
        self._list.addFirst(e)

    # 元素出栈，同时返回栈顶元素
    def pop(self):
        return self._list.removeFirst()

    # 查看栈顶元素，不出栈
    def peek(self):
        return self._list.getFirst()

    def __str__(self):
        return "LinkedListStack: top " + self._list.getString()


