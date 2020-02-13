# coding=utf-8


class LinkedListMap:

    class __Node:
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next
    """
    时间复杂度分析：
    添加操作：addLast(e):O(n)    addFirst(e):O(1)    add(index, e):O(n/2)=O(n)
    删除操作：removeLast(e):O(n)    removeFirst(e):O(1)    remove(index, e):O(n/2)=O(n)
    修改操作：set(index, e):O(n)
    查找操作：get(index):O(n)    contains(e):O(n)
    """
    def __init__(self):
        self.__dummyHead = self.__Node()
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def add(self, key, value):
        node = self.__getNode(key)
        if node == None:
            self.__dummyHead.next = self.__Node(key, value, self.__dummyHead.next)
            self.__size += 1
        else:  # key已经存在，更新(key,value)对
            node.value = value

    def remove(self, key):
        prev = self.__dummyHead
        while prev.next != None:
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
        if node == None:
            raise Exception(str(key) + " does't exist!")
        node.value = value

    def get(self, key):
        node = self.__getNode(key)
        if node == None:
            return None
        else:
            return node.value

    def contains(self, key):
        return self.__getNode(key) != None

    def __getNode(self, key):
        cur = self.__dummyHead
        while cur != None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

