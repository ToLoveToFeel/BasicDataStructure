# coding=utf-8


class SegmentTree:
    """
    时间复杂度分析：n为数组大小
        更新set：O(logn)
        查询query：O(logn)
    空间复杂度分析：n为数组大小
        O(n)
    """
    def __init__(self, arr, merger=(lambda a, b: a + b)):
        self.__data = arr
        self.__tree = [None for _ in range(len(arr) * 4)]
        self.__merger = merger  # merger是lambda表达式
        self.__buildSegmentTree(0, 0, len(arr) - 1)  # 创建线段树

    # 在treeIndex的位置创建表示区间[l...r]的线段树
    def __buildSegmentTree(self, treeIndex, l, r):
        if l == r:
            self.__tree[treeIndex] = self.__data[l]
            return

        leftTreeIndex = self.__leftChild(treeIndex)
        rightTreeIndex = self.__rightChild(treeIndex)

        mid = l + int((r - l) / 2)
        self.__buildSegmentTree(leftTreeIndex, l, mid)
        self.__buildSegmentTree(rightTreeIndex, mid + 1, r)

        self.__tree[treeIndex] = self.__merger(self.__tree[leftTreeIndex], self.__tree[rightTreeIndex])

    def getSize(self):
        return len(self.__data)

    def get(self, index):
        if index < 0 or index >= len(self.__data):
            raise Exception("Index is illegal.")
        return self.__data[index]

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    def __leftChild(self, index):
        return 2 * index + 1

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    def __rightChild(self, index):
        return 2 * index + 2

    # 返回区间[queryL, queryR]的值
    def query(self, queryL, queryR):
        if queryL < 0 or queryL > len(self.__data) or queryR < 0 or queryR > len(self.__data):
            raise Exception("Index is illegal.")
        return self.__query(0, 0, len(self.__data) - 1, queryL, queryR)

    # 在以treeIndex为根的线段树中[l...r]的范围里，搜索区间[queryL...queryR]的值
    def __query(self, treeIndex, l, r, queryL, queryR):
        if l == queryL and r == queryR:
            return self.__tree[treeIndex]

        # treeIndex的节点分为[l...mid]和[mid+1...r]两部分
        mid = l + int((r - l) / 2)
        leftTreeIndex = self.__leftChild(treeIndex)
        rightTreeIndex = self.__rightChild(treeIndex)
        if queryL >= mid + 1:
            return self.__query(rightTreeIndex, mid + 1, r, queryL, queryR)
        elif queryR <= mid:
            return self.__query(leftTreeIndex, l, mid, queryL, queryR)

        leftResult = self.__query(leftTreeIndex, l, mid, queryL, mid)
        rightResult = self.__query(rightTreeIndex, mid + 1, r, mid + 1, queryR)

        return self.__merger(leftResult, rightResult)

    # 将index位置的值，更新为e
    def set(self, index, e):
        if index < 0 or index >= len(self.__data):
            raise Exception("Index is illegal.")
        self.__data[index] = e
        self.__set(0, 0, len(self.__data) - 1, index, e)

    # 在以treeIndex为根的线段树中更新index的值为e
    def __set(self, treeIndex, l, r, index, e):
        if l == r:
            self.__tree[treeIndex] = e
            return

        # treeIndex的节点分为[l...mid]和[mid+1...r]两部分
        mid = l + int((r - l) / 2)
        leftTreeIndex = self.__leftChild(treeIndex)
        rightTreeIndex = self.__rightChild(treeIndex)
        if index >= mid + 1:
            self.__set(rightTreeIndex, mid + 1, r, index, e)
        else:  # index < mid + 1
            self.__set(leftTreeIndex, l, mid, index, e)

        self.__tree[treeIndex] = self.__merger(self.__tree[leftTreeIndex], self.__tree[rightTreeIndex])

    def __str__(self):
        res = "["
        for i in range(len(self.__tree)):
            if self.__tree[i] != None:
                res += str(self.__tree[i])
            else:
                res += "None"

            if i != len(self.__tree) - 1:
                res += ", "
        res += "]"
        return res



