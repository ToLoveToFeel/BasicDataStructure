# coding=utf-8
import numpy as np


class UFNumpy:
    """
    效率更低下
    时间复杂度分析：h为树的高度
        unionElements(p, q)：O(h)
        isConnected(p, q)：O(h)
    """
    def __init__(self, size):
        self.__parent = np.arange(size, dtype=int)  # 记录指向的父亲节点
        self.__rank = np.ones(shape=size, dtype=int)  # rank[i]表示以i为根的集合所表示的树的层数

    # 获取并查集元素个数
    def getSize(self):
        return len(self.__parent)

    # 辅助函数，查找元素p所对应的集合编号，O(h)复杂度，h为树高
    def __find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound!")
        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]  # 路径压缩
            p = self.__parent[p]
        return p

    # # 辅助函数，查找元素p所对应的集合编号，O(h)复杂度，h为树高，压缩为两层
    # def __find(self, p):
    #     if p < 0 or p >= len(self.__parent):
    #         raise Exception("p is out of bound!")
    #     if p != self.__parent[p]:
    #         self.__parent[p] = self.__find(self.__parent[p])  # 路径压缩
    #     return self.__parent[p]

    # 判断两个元素是否相连
    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并两个集合
    def unionElements(self, p, q):
        pRoot = self.__find(p)
        qRoot = self.__find(q)

        if pRoot == qRoot:
            return

        # 根据两个元素所在树的rank不同判断合并方向
        # 将rank低的集合并到rank高的集合上
        if self.__rank[pRoot] < self.__rank[qRoot]:
            self.__parent[pRoot] = qRoot  # 让pRoot指向qRoot
        elif self.__rank[pRoot] > self.__rank[qRoot]:
            self.__parent[qRoot] = pRoot  # 让pRoot指向qRoot
        else:  # self.__rank[pRoot] == self.__rank[qRoot]
            self.__parent[qRoot] = pRoot
            self.__rank[pRoot] += 1



