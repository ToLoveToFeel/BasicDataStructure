# coding=utf-8
import numpy as np


class Array:
    """
                              _size
    data | 66 | 77 | 88 | 99 |    |    |    |  capacity
    """
    # 构造函数
    def __init__(self, capacity=10, dtype="int"):
        self._data = np.zeros(shape=capacity, dtype=eval(dtype))
        self._size = 0  # 数组实际大小
        self._dtype = dtype

    # 返回数组中元素个数，覆盖len(u)方法，u为该类的对象
    def __len__(self):
        return self._size

    # 返回数组中元素个数
    def getSize(self):
        return self._size

    # 获取数组的容量
    def getCapacity(self):
        return len(self._data)

    # 返回数组是否为空
    def isEmpty(self):
        return self._size == 0

    # 向所有元素后添加一个元素
    def addLast(self, e):
        self.add(self._size, e)

    # 在所有元素前添加一个新元素
    def addFirst(self, e):
        self.add(0, e)

    # 在第index个位置插入一个新元素e
    def add(self, index, e):
        # assert 条件为False时执行
        assert not (index < 0 or index > self._size), "Add failed. Requre index >= 0 and index <= size."

        if self._size == len(self._data):  # 扩容
            self.__resize(2 * len(self._data))

        for i in range(self._size-1, index-1, -1):  # [self._size-1...index]
            self._data[i+1] = self._data[i]

        self._data[index] = e
        self._size += 1

    # 获取index索引位置的元素
    def get(self, index):
        assert not (index < 0 or index >= self._size), "Get failed. Index is illegal."
        return self._data[index]

    # 修改index索引位置的元素为e
    def set(self, index, e):
        assert not (index < 0 or index >= self._size), "Set failed. Index is illegal."
        self._data[index] = e

    # 查找数组中是否有元素e
    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False

    # 查找数组中元素e所在的索引，如果不存在元素e，返回-1
    def find(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    # 从数组中删除index位置的元素，返回删除的元素
    def remove(self, index):
        assert not (index < 0 or index >= self._size), "Set failed. Index is illegal."

        ret = self._data[index]
        for i in range(index+1, self._size):
            self._data[i-1] = self._data[i]
        self._size -= 1

        if self._size == int(len(self._data) / 2):  # 缩容
            self.__resize(int(len(self._data) / 2))

        return ret

    # 从数组中删除第一个元素，返回删除的元素
    def removeFirst(self):
        return self.remove(0)

    # 从数组中删除最后一个元素，返回删除的元素
    def removeLast(self):
        return self.remove(self._size-1)

    # 从数组中删除元素e
    def removeElement(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    # 用户调用print(u)输出的字符串形式，u为该类的对象
    def __str__(self):
        res = "Array: size = {0} , capacity = {1}\n".format(self._size, len(self._data))
        res += "["
        for i in range(self._size):
            res += str(self._data[i])
            if i != self._size - 1:
                res += ", "
        res += "]"
        return res

    # 私有函数
    def __resize(self, newCapacity):
        newData = np.zeros(shape=newCapacity, dtype=eval(self._dtype))
        for i in range(self._size):
            newData[i] = self._data[i]
        del(self._data)
        self._data = newData


