# coding=utf-8


class LinkedList:

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
        self._dummyHead = self.__Node()
        self._size = 0

    # 获取链表中的元素的个数
    def getSize(self):
        return self._size

    # 判断链表是否为空
    def isEmpty(self):
        return self._size == 0

    # 在链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用
    def add(self, index, e):
        assert not (index < 0 or index > self._size), "Add failed. Illegal index."

        prev = self._dummyHead
        for i in range(index):
            prev = prev.next

        # node = self.__Node(element=e)
        # node.next = prev.next()
        # prev.next = node
        prev.next = self.__Node(e, prev.next)
        self._size += 1

    # 在链表头添加元素
    def addFirst(self, e):
        self.add(0, e)

    # 在链表的末尾添加新的元素e
    def addLast(self, e):
        self.add(self._size, e)

    # 获得链表的第index(0-based)个位置的元素
    # 在链表中不是一个常用的操作，练习用
    def get(self, index):
        assert not (index < 0 or index >= self._size), "Add failed. Illegal index."

        cur = self._dummyHead.next
        for i in range(index):
            cur = cur.next
        return cur.e

    # 获得链表的第一个元素
    def getFirst(self):
        return self.get(0)

    # 获取链表的最后一个元素
    def getLast(self):
        return self.get(self._size - 1)

    # 修改链表的第ndex(0-based)个位置的元素为e
    # 在链表中不是一个常用的操作，练习用
    def set(self, index, e):
        assert not (index < 0 or index >= self._size), "Add failed. Illegal index."
        cur = self._dummyHead.next
        for i in range(index):
            cur = cur.next
        cur.e = e

    # 在链表中查找是否有元素e
    def contains(self, e):
        cur = self._dummyHead
        while cur != None:
            if cur.e == e:
                return True
            cur = cur.next
        return False

    # 从链表删除index(0-based)位置的元素，返回删除的元素
    # 在链表中不是一个常用的操作，练习用
    def remove(self, index):
        assert not (index < 0 or index >= self._size), "Add failed. Illegal index."
        prev = self._dummyHead
        for i in range(index):
            prev = prev.next

        retNode = prev.next
        prev.next = retNode.next
        retNode.next = None
        self._size -= 1

        retValue = retNode.e
        del(retNode)
        return retValue

    # 从链表中删除第一个元素，返回删除的元素
    def removeFirst(self):
        return self.remove(0)

    # 从链表中删除最后一个元素，返回删除的元素
    def removeLast(self):
        return self.remove(self._size - 1)

    # 从链表中删除元素e
    def removeElement(self, e):
        prev = self._dummyHead
        while prev.next != None:
            if prev.next.e == e:
                break
            prev = prev.next

        if prev.next != None:
            delNode = prev.next
            prev.next = delNode.next
            del delNode
            self._size -= 1

    def __str__(self):
        return self.getString()

    def getString(self):
        res = ""
        cur = self._dummyHead.next
        while cur != None:
            res = res + str(cur.e) + "->"
            cur = cur.next
        res += "NULL"
        return res




