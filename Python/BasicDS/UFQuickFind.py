# coding=utf-8
# @Time       : 2020/2/16
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : UFQuickFind.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


class UFQuickFind:
    """
    时间复杂度分析：
        unionElements(p, q)：O(n)
        isConnected(p, q)：O(1)
    """
    def __init__(self, size):
        self.__id = [i for i in range(size)]

    # 获取并查集元素个数
    def getSize(self):
        return len(self.__id)

    # 辅助函数，找出id[i]所对应的id
    def __find(self, p):
        if p < 0 or p >= len(self.__id):
            raise Exception("p is out of bound!")
        return self.__id[p]

    # 判断两个元素是否相连
    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并两个集合
    def unionElements(self, p, q):
        pID = self.__find(p)
        qID = self.__find(q)

        if pID == qID:
            return

        for i in range(len(self.__id)):
            if self.__id[i] == pID:
                self.__id[i] = qID


