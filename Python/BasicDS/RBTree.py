# coding=utf-8
# @Time       : 2020/2/17
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : RBTree.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


class RBTree:  # 红黑树
    """
    《算法导论》中红黑树的定义是满足下面五点的一种树结构：
            1.每个节点或者是红色的，或者是黑色的
            2.根节点是黑色的
            3.每个叶子节点（最后的空节点）是黑色的
            4.如果一个节点是红色的，那么他的孩子节点都是黑色的
            5.从任意一个节点到叶子节点，经过的黑色节点是一样的
    """
    RED = True  # 常量，代表红色节点
    BLACK = False  # 常量，代表黑色节点

    class __Node:
        def __init__(self, key=None, value=None, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.color = RBTree.RED

    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__treeString = ""

    # 获取红黑树中的元素的个数
    def getSize(self):
        return self.__size

    # 判断红黑树是否为空
    def isEmpty(self):
        return self.__size == 0

    # 判断节点node的颜色
    def __isRed(self, node):
        if node is None:
            return RBTree.BLACK
        return node.color

    # 插入x（红色），若x的插入位置是node的右侧，则需要左旋转，这只是其中一步
    # 此时可能出现x和node均为红色节点，但没关系，后续还需要处理
    # node的右孩子为红色，左孩子不为红色（否则左孩子为红色的话，node一定为黑色，此时需要做的是颜色翻转）
    #   node                     x
    #  /   \     左旋转         /  \
    # T1   x   --------->   node   T3
    #     / \              /   \
    #    T2 T3            T1   T2
    def __leftRotate(self, node):
        # 暂存信息
        x = node.right

        # 向左旋转过程
        node.right = x.left
        x.left = node

        # 重新染色，考虑红黑树与2-3树的等价性，此时该节点变为一个三节点
        x.color = node.color
        node.color = RBTree.RED

        return x

    # 插入y（红色），若y的插入位置是x的左侧，且x是红色节点需要右旋转，这只是其中一步
    # 此时可能出现x和node均为红色节点，但没关系，后续还需要处理
    # node为黑色，x,y为红色，此时需要右旋转 后 颜色翻转
    #     node                   x
    #    /   \     右旋转       /  \
    #   x    T2   ------->   y   node
    #  / \                       /  \
    # y  T1                     T1  T2
    def __rightRotate(self, node):
        # 暂存信息
        x = node.left

        # 向左旋转过程
        node.left = x.right
        x.right = node

        # 重新染色，考虑红黑树与2-3树的等价性，此时该节点变为一个三节点
        x.color = node.color
        node.color = RBTree.RED

        return x

    # 颜色翻转，调用该函数，必须保证符合相应条件：插入y后，x,y是红色，node是黑色
    # 翻转之后，x,y是黑色，node是红色
    #   node                     node
    #  /   \     左旋转         /  \
    # x    y   --------->     x    y
    def __flipColors(self, node):
        node.color = RBTree.RED
        node.left.color = RBTree.BLACK
        node.right.color = RBTree.BLACK

    # 向红黑树中添加元素(key, value)
    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)
        self.__root.color = RBTree.BLACK  # 根节点始终未黑色

    # 向以node为根节点的红黑树中添加元素(key, value)，递归算法
    # 返回插入新节点后红黑树的根
    def __add(self, node, key, value):
        if node is None:
            self.__size += 1
            return self.__Node(key=key, value=value)  # 默认插入红色节点

        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else:  # key == node.key
            node.value = value

        # 判断是否左旋转，左黑右红
        if (not self.__isRed(node.left)) and self.__isRed(node.right):
            node = self.__leftRotate(node)
        # 判断是否右旋转，左红左左红
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rightRotate(node)
        # 判断是否颜色翻转，左红右红
        if self.__isRed(node.left) and self.__isRed(node.right):
            self.__flipColors(node)

        return node

    def set(self, key, value):
        node = self.__getNode(self.__root, key)
        if node is None:
            raise Exception(str(key) + " does't exist!")
        node.value = value

    def get(self, key):
        node = self.__getNode(self.__root, key)
        if node is None:
            return None
        else:
            return node.value

    def contains(self, key):
        return self.__getNode(self.__root, key) is not None

    # 返回以node为根节点的红黑树中，key所在的节点
    def __getNode(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self.__getNode(node.left, key)
        else:  # key > node.key
            return self.__getNode(node.right, key)

