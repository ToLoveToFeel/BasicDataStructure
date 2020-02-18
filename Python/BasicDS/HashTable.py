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
    """
    均摊复杂度分析：
        O(1)
    哈希表速度虽然很快，但哈希表失去了顺序性
    """
    # 常量
    capacity= [
        53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593,
        49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469,
        12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741
    ]
    upperTol = 10  # 扩容
    lowerTol = 2  # 缩容
    # 变量
    capacityIndex = 0

    def __init__(self):
        self.__M = HashTable.capacity[HashTable.capacityIndex]
        self.__hashtable = [AVLTreeMap() for _ in range(self.__M)]
        self.__size = 0

    # 产生哈希值
    def __hash(self, key):
        return abs(hash(key)) % self.__M

    # 获取元素个数
    def getSize(self):
        return self.__size

    # 判断是否为空
    def isEmpty(self):
        for i in range(self.__M):
            if not self.__hashtable[i].isEmpty():
                return False
        return True

    # 向哈希表中添加元素
    def add(self, key, value):
        map = self.__hashtable[self.__hash(key)]
        if map.contains(key):
            map.set(key, value)
        else:
            map.add(key, value)
            self.__size += 1
            if self.__size >= HashTable.upperTol * self.__M and HashTable.capacityIndex + 1 < len(HashTable.capacity):
                HashTable.capacityIndex += 1
                self.__resize(HashTable.capacity[HashTable.capacityIndex])

    # 从哈希表中删除元素
    def remove(self, key):
        map = self.__hashtable[self.__hash(key)]
        ret = None
        if map.contains(key):
            ret = map.remove(key)
            self.__size -= 1
            if self.__size < HashTable.lowerTol * self.__M and HashTable.capacityIndex - 1 >= 0:
                HashTable.capacityIndex -= 1
                self.__resize(HashTable.capacity[HashTable.capacityIndex])
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

    # hashset元素个数
    def getHashSetSize(self):
        size = 0
        for i in range(self.__M):
            size += self.__hashtable[i].getSize()
        return size
