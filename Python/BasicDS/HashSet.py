# coding=utf-8
# @Time       : 2020/2/18
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : HashSet.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure
from BasicDS.HashTable import HashTable


class HashSet:
    def __init__(self):
        self.__hashset = HashTable()

    def getSize(self):
        return self.__hashset.getUniqueSize()

    def isEmpty(self):
        return self.__hashset.isEmpty()

    def add(self, e):
        if not self.__hashset.contains(e):
            self.__hashset.add(e, None)

    def contains(self, e):
        return self.__hashset.contains(e)

    def remove(self, e):
        self.__hashset.remove(e)


