# coding=utf-8
from BasicDS.LinkedList import LinkedList


class LinkedListSet:
    def __init__(self):
        self.__list = LinkedList()

    def getSize(self):
        return self.__list.getSize()

    def isEmpty(self):
        return self.__list.isEmpty()

    def add(self, e):
        if not self.__list.contains(e):
            self.__list.addLast(e)

    def contains(self, e):
        self.__list.contains(e)

    def remove(self, e):
        self.__list.removeElement(e)

