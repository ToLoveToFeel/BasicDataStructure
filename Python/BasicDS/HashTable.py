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

    def __init__(self, M=97):
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

    # 从哈希表中删除元素
    def remove(self, key):
        map = self.__hashtable[self.__hash(key)]
        ret = None
        if map.contains(key):
            ret = map.remove(key)
            self.__size -= 1
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
