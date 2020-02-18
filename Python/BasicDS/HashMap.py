# coding=utf-8
# @Time       : 2020/2/18
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : HashMap.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.HashTable import HashTable


class HashMap:
    def __init__(self):
        self.__hashmap = HashTable()

    def getSize(self):
        return self.__hashmap.getUniqueSize()

    def isEmpty(self):
        return self.__hashmap.isEmpty()

    def add(self, key, value):
        self.__hashmap.add(key, value)

    def remove(self, key):
        self.__hashmap.remove(key)

    def set(self, key, value):
        self.__hashmap.set(key, value)

    def get(self, key):
        return self.__hashmap.get(key)

    def contains(self, key):
        return self.__hashmap.contains(key)

    def keySet(self):
        return self.__hashmap.keySet()
