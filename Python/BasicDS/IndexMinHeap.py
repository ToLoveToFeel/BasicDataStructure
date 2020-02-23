# coding=utf-8
# @Time       : 2020/2/23
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : IndexMinHeap.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


class IndexMinHeap:
    """
    最小索引堆：参考最大索引堆
    """
    def __init__(self, capacity=10):
        self.__data = [0 for _ in range(capacity)]  # 最小索引堆中的数据
        self.__indexes = [-1 for _ in range(capacity)]
        self.__reverse = [-1 for _ in range(capacity)]

        self.__count = 0  # 堆中数据的个数
        self.__capacity = capacity  # 堆的容量

    # 返回索引堆中的元素个数
    def getSize(self):
        return self.__count

    # 返回一个布尔值，表示索引堆中是否为空
    def isEmpty(self):
        return self.__count == 0

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    def __parent(self, index):
        if index == 0:
            raise Exception("index-0 doesn't have parent.")
        return int((index - 1) / 2)

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    def __leftChild(self, index):
        return index * 2 + 1

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    def __rightChild(self, index):
        return index * 2 + 2

    # 看索引i所在的位置是否存在元素
    def contains(self, i):
        if i < 0 or i >= self.__capacity:
            raise Exception("Index is out of range!")
        return self.__reverse[i] != -1

    # 向最大索引堆中插入一个新的元素, 新元素的索引为i, 元素为item
    def add(self, i, item):
        if self.__count > self.__capacity:
            raise Exception("No space!")
        # 再插入一个新元素前,还需要保证索引i所在的位置是没有元素的
        if self.contains(i):
            raise Exception("can't add " + item + " in index " + i + ",because there has an element!")
        self.__data[i] = item
        self.__indexes[self.__count] = i
        self.__reverse[i] = self.__count
        self.__siftUp(self.__count)
        self.__count += 1

    # 索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
    def __siftUp(self, k):
        while k > 0 and self.__data[(self.__indexes[self.__parent(k)])] > self.__data[(self.__indexes[k])]:
            self.__indexes[self.__parent(k)], self.__indexes[k] = self.__indexes[k], self.__indexes[self.__parent(k)]  # 交换
            self.__reverse[self.__indexes[self.__parent(k)]] = self.__parent(k)
            self.__reverse[self.__indexes[k]] = k
            k = self.__parent(k)

    # 取出索引堆中最小元素
    def extractMin(self):
        if self.__count == 0:
            raise Exception("Cannot extractMax when heap is empty!")
        ret = self.__data[self.__indexes[0]]
        self.__indexes[0], self.__indexes[self.__count - 1] = self.__indexes[self.__count - 1], self.__indexes[0]
        self.__reverse[self.__indexes[self.__count - 1]] = -1
        self.__count -= 1
        if self.__count != 0:
            self.__reverse[self.__indexes[0]] = 0
            self.__siftDown(0)

        return ret

    # 索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
    def __siftDown(self, k):
        while self.__leftChild(k) < self.__count:
            j = self.__leftChild(k)
            if (j + 1 < self.__count) and (self.__data[(self.__indexes[j + 1])] < self.__data[(self.__indexes[j])]):
                j = self.__rightChild(k)
            # self.__data.get(j)是leftChild和rightChild中的最大值
            if self.__data[(self.__indexes[k])] < self.__data[(self.__indexes[j])]:
                break

            self.__indexes[j], self.__indexes[k] = self.__indexes[k], self.__indexes[j]
            self.__reverse[self.__indexes[k]] = k
            self.__reverse[self.__indexes[j]] = j
            k = j

    # 看索引堆中的最大元素
    def findMin(self):
        if self.__count == 0:
            raise Exception("Cannot findMin when heap is empty!")
        return self.__data[(self.__indexes[0])]

    # 获取最大索引堆中的堆顶元素的索引
    def findMinIndex(self):
        if self.__count == 0:
            raise Exception("Cannot findMin when heap is empty!")
        return self.__indexes[0]

    # 获取最大索引堆中索引为i的元素
    def getItem(self, i):
        if not self.contains(i):
            raise Exception("there has no element!")
        return self.__data[i]

    # 将最小索引堆中索引为i的元素修改为newItem
    def change(self, i, newItem):
        if not self.contains(i):
            raise Exception("there has no element!")
        self.__data[i] = newItem
        # 我们可以非常简单的通过reverse直接定位索引i在indexes中的位置
        self.__siftUp(self.__reverse[i])
        self.__siftDown(self.__reverse[i])

    # 取出索引堆中的最小元素，并且替换成元素e
    def replace(self, e):
        ret = self.findMin()
        self.change(self.__indexes[0], e)
        return ret

