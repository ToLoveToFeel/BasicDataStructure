# coding=utf-8
from BasicDS.BSTMap import BSTMap


class Trie:

    class __Node:
        def __init__(self, isWord=False):
            self.isWord = isWord  # 记录走到当前位置是否为单词
            self.next = BSTMap()  # 记录当前字符的孩子节点

    def __init__(self):
        self.__root = self.__Node()  # 根节点
        self.__size = 0  # 当前字典树中单词的个数

    # 获得Trie中存储的单词数量
    def getSize(self):
        return self.__size

    # 向Trie中添加一个新的单词word
    def add(self, word):
        cur = self.__root
        for c in word:
            if cur.next.get(c) == None:  # 当前映射中不包含c
                cur.next.add(c, self.__Node())
            cur = cur.next.get(c)  # 获取字符c对应的下一个节点
        if not cur.isWord:
            cur.isWord = True
            self.__size += 1

    # 查询单词word是否在Trie中
    def contains(self, word):
        cur = self.__root
        for c in word:
            if cur.next.get(c) == None:
                return False
            cur = cur.next.get(c)
        return cur.isWord







