# coding=utf-8


class Array:
    """
                              __size
    data | 66 | 77 | 88 | 99 |    |    |    |  capacity
    复杂度分析：
    增：O(n)
    删：O(n)
    改：已知索引O(1)，未知索引O(n)
    查：已知索引O(1)，未知索引O(n)
    """
    # 构造函数
    def __init__(self, capacity=10):
        self.__data = [0 for _ in range(capacity)]
        self.__size = 0  # 数组实际大小

    # 返回数组中元素个数，覆盖len(u)方法，u为该类的对象
    def __len__(self):
        return self.__size

    # 返回数组中元素个数
    def getSize(self):
        return self.__size

    # 获取数组的容量
    def getCapacity(self):
        return len(self.__data)

    # 返回数组是否为空
    def isEmpty(self):
        return self.__size == 0

    # 向所有元素后添加一个元素
    def addLast(self, e):
        self.add(self.__size, e)

    # 在所有元素前添加一个新元素
    def addFirst(self, e):
        self.add(0, e)

    # 在第index个位置插入一个新元素e
    def add(self, index, e):
        # assert 条件为False时执行
        assert not (index < 0 or index > self.__size), "Add failed. Requre index >= 0 and index <= size."

        if self.__size == len(self.__data):  # 扩容
            self.__resize(2 * len(self.__data))

        for i in range(self.__size-1, index-1, -1):  # [self.__size-1...index]
            self.__data[i+1] = self.__data[i]

        self.__data[index] = e
        self.__size += 1

    # 获取index索引位置的元素
    def get(self, index):
        assert not (index < 0 or index >= self.__size), "Get failed. Index is illegal."
        return self.__data[index]

    # 获取第一个元素
    def getFirst(self):
        return self.get(self.__size - 1)

    # 获取最后一个元素
    def getLast(self):
        return self.get(0)

    # 修改index索引位置的元素为e
    def set(self, index, e):
        assert not (index < 0 or index >= self.__size), "Set failed. Index is illegal."
        self.__data[index] = e

    # 查找数组中是否有元素e
    def contains(self, e):
        for i in range(self.__size):
            if self.__data[i] == e:
                return True
        return False

    # 查找数组中元素e所在的索引，如果不存在元素e，返回-1
    def find(self, e):
        for i in range(self.__size):
            if self.__data[i] == e:
                return i
        return -1

    # 从数组中删除index位置的元素，返回删除的元素
    def remove(self, index):
        assert not (index < 0 or index >= self.__size), "Set failed. Index is illegal."

        ret = self.__data[index]
        for i in range(index+1, self.__size):
            self.__data[i-1] = self.__data[i]
        self.__size -= 1

        if (self.__size == int(len(self.__data) / 4)) and (int(len(self.__data) / 2) != 0):  # 缩容，Lazy，防止复杂度震荡
            self.__resize(int(len(self.__data) / 2))

        return ret

    # 从数组中删除第一个元素，返回删除的元素
    def removeFirst(self):
        return self.remove(0)

    # 从数组中删除最后一个元素，返回删除的元素
    def removeLast(self):
        return self.remove(self.__size-1)

    # 从数组中删除元素e
    def removeElement(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    # 用户调用print(u)输出的字符串形式，u为该类的对象
    def __str__(self):
        res = "Array: size = {0} , capacity = {1}\n".format(self.__size, len(self.__data))
        res += "["
        for i in range(self.__size):
            res += str(self.__data[i])
            if i != self.__size - 1:
                res += ", "
        res += "]"
        return res

    # 私有函数
    def __resize(self, newCapacity):
        newData = [0 for _ in range(newCapacity)]
        for i in range(self.__size):
            newData[i] = self.__data[i]
        del(self.__data)
        self.__data = newData


