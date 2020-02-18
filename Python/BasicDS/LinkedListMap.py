# coding=utf-8
# @Time       : 2020/2/13
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : LinkedListMap.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


class LinkedListMap:
    """
    时间复杂度分析(平均)：n为元素个数
    增 add：O(n)
    删 remove：O(n)
    改 set：O(n)
    查 get：O(n)      contains：O(n)
    """
    class __Node:
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self.__dummyHead = self.__Node()
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def add(self, key, value):
        node = self.__getNode(key)
        if node is None:
            self.__dummyHead.next = self.__Node(key, value, self.__dummyHead.next)
            self.__size += 1
        else:  # key已经存在，更新(key,value)对
            node.value = value

    def remove(self, key):
        prev = self.__dummyHead
        while prev.next is not None:
            if prev.next.key == key:
                break
            prev = prev.next

        if prev.next != None:
            delNode = prev.next
            delValue = delNode.value
            prev.next = delNode.next
            del delNode
            self.__size -= 1
            return delValue
        return None

    def set(self, key, value):
        node = self.__getNode(key)
        if node is None:
            raise Exception(str(key) + " does't exist!")
        node.value = value

    def get(self, key):
        node = self.__getNode(key)
        if node is None:
            return None
        else:
            return node.value

    def contains(self, key):
        return self.__getNode(key) is not None

    def __getNode(self, key):
        cur = self.__dummyHead
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

