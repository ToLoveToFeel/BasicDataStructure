# coding=utf-8
# @Time       : 2020/2/13
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : BSTMap.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


class BSTMap:
    """
    时间复杂度分析(平均)：n为元素个数
    增 add：O(logn)
    删 remove：O(logn)
    改 set：O(logn)
    查 get：O(logn)      contains：O(logn)
    """
    class __Node:
        def __init__(self, key=None, value=None, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__treeString = ""

    # 获取二分搜索树中的元素的个数
    def getSize(self):
        return self.__size

    # 判断二分搜索树是否为空
    def isEmpty(self):
        return self.__size == 0

    # 向二分搜索树中添加元素(key, value)
    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)

    # 向以node为根节点的二分搜索树中添加元素(key, value)，递归算法
    # 返回插入新节点后二分搜索树的根
    def __add(self, node, key, value):
        if node is None:
            self.__size += 1
            return self.__Node(key=key, value=value)

        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else:  # key == node.key
            node.value = value

        return node

    def remove(self, key):
        node = self.__getNode(self.__root, key)
        if node is not None:
            self.__root = self.__remove(self.__root, key)
            return node.value
        return None

    # 返回以node为根的二分搜索树的最小值所在的节点，递归算法
    def __minimum(self, node):
        if node.left is None:
            return node
        return self.__minimum(node.left)

    # 删除以node为根的二分搜索树中的最小节点
    # 返回删除节点后新的二分搜索树的根
    def __removeMin(self, node):
        if node.left is None:
            rightNode = node.right
            # node.right = None
            del node
            self.__size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    # 从二分搜索树中删除键为e的节点，递归算法
    # 返回删除节点后新的二分搜索树的根
    def __remove(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:  # key == node.key
            # 待删除节点左子树为空的情况
            if node.left is None:
                rightNode = node.right
                # node.right = None
                del node
                self.__size -= 1
                return rightNode
            # 待删除节点右子树为空的情况
            if node.right is None:
                leftNode = node.left
                # node.left = None
                del node
                self.__size -= 1
                return leftNode
            # 待删除节点左右子树均不为为空的情况
            # 找到比待删除节点大的最小节点, 即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self.__minimum(node.right)  # 获取node右子树最小值
            successor.right = self.__removeMin(node.right)  # 删除node右子树最小值，同时挂接右子树
            successor.left = node.left  # 挂接左子树
            node.left = node.right = None
            # del node  # 删除node

            return successor

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

    # 返回以node为根节点的二分搜索树中，key所在的节点
    def __getNode(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self.__getNode(node.left, key)
        else:  # key > node.key
            return self.__getNode(node.right, key)

