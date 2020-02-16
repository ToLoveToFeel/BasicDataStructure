# coding=utf-8


class UF:
    """
    时间复杂度分析：h为树的高度
        unionElements(p, q)：O(h)
        isConnected(p, q)：O(h)
    """
    def __init__(self, size):
        self.__parent = [i for i in range(size)]  # 记录指向的父亲节点

    # 获取并查集元素个数
    def getSize(self):
        return len(self.__parent)

    # 辅助函数，查找元素p所对应的集合编号，O(h)复杂度，h为树高
    def __find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound!")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p

    # 判断两个元素是否相连
    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并两个集合
    def unionElements(self, p, q):
        pRoot = self.__find(p)
        qRoot = self.__find(q)

        if pRoot == qRoot:
            return

        self.__parent[pRoot] = qRoot  # 让pRoot指向qRoot


