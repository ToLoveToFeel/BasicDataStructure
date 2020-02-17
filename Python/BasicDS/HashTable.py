# coding=utf-8
# @Time       : 2020/2/17
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : HashTable.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.AVLTreeMap import AVLTreeMap
# https://planetmath.org/goodhashtableprimes  素数(M)的选择


class HashTable:
    # 常量
    upperTol = 10  # 扩容
    lowerTol = 2  # 缩容
    initCapacity = 7

    def __init__(self, M=initCapacity):
        self.__hashtable = [AVLTreeMap() for _ in range(M)]
        self.__M = M
        self.__size = 0

    # 产生哈希值
    def __hash(self, key):
        return abs(hash(key)) % self.__M

    # 获取元素个数
    def getSize(self):
        return self.__size

    # 向哈希表中添加元素
    def add(self, key, value):
        map = self.__hashtable[self.__hash(key)]
        if map.contains(key):
            map.set(key, value)
        else:
            map.add(key, value)
            self.__size += 1
            if self.__size >= HashTable.upperTol * self.__M:
                self.__resize(2 * self.__M)

    # 从哈希表中删除元素
    def remove(self, key):
        map = self.__hashtable[self.__hash(key)]
        ret = None
        if map.contains(key):
            ret = map.remove(key)
            self.__size -= 1
            if self.__size < HashTable.lowerTol * self.__M and self.__M / 2 >= HashTable.initCapacity:
                self.__resize(int(self.__M / 2))
        return ret

    # 更改哈希表中的元素
    def set(self, key, value):
        map = self.__hashtable[self.__hash(key)]
        if not map.contains(key):
            raise Exception(str(key) + " does't exist!")
        map.set(key, value)

    # 查找哈希表中是否包含某元素
    def contains(self, key):
        return self.__hashtable[self.__hash(key)].contains(key)

    # 查找哈希表中键所对应的值
    def get(self, key):
        return self.__hashtable[self.__hash(key)].get(key)

    # 动态容量
    def __resize(self, newM):
        newHashTable = [AVLTreeMap() for _ in range(newM)]

        oldM = self.__M
        self.__M = newM
        for i in range(oldM):
            map = self.__hashtable[i]
            for key in map.keySet():
                newHashTable[self.__hash(key)].add(key, map.get(key))

        self.__hashtable = newHashTable

