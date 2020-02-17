# coding=utf-8


class LinkedListQueue:

    class __Node:
        def __init__(self, element=None, next=None):
            self.e = element
            self.next = next
    """
    时间复杂度分析：
    添加操作：addLast(e):O(n)    addFirst(e):O(1)    add(index, e):O(n/2)=O(n)
    删除操作：removeLast(e):O(n)    removeFirst(e):O(1)    remove(index, e):O(n/2)=O(n)
    修改操作：set(index, e):O(n)
    查找操作：get(index):O(n)    contains(e):O(n)
    """
    def __init__(self):
        self._head = None  # 队列头
        self._tail = None  # 队列尾
        self._size = 0

    # 获取链表中的元素的个数
    def getSize(self):
        return self._size

    # 判断链表是否为空
    def isEmpty(self):
        return self._size == 0

    # 入队
    def enqueue(self, e):
        if self._tail is None:
            self._tail = self.__Node(element=e)
            self._head = self._tail
        else:
            self._tail.next = self.__Node(element=e)
            self._tail = self._tail.next
        self._size += 1

    # 元素出队，同时返回队首元素
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue from an empty queue.")

        retNode = self._head
        self._head = self._head.next
        retNode.next = None
        if self._head is None:
            self._tail = None

        retValue = retNode.e
        del retNode
        self._size -= 1

        return retValue

    # 查看队首元素，不出队
    def getFront(self):
        assert not self.isEmpty(), "Queue is empty."
        return self._head.e

    def __str__(self):
        res = "LinkedListQueue: front "
        cur = self._head
        while cur is not None:
            res = res + str(cur.e) + "->"
            cur = cur.next
        res += "NULL tail"
        return res
