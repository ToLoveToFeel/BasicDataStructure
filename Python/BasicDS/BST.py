# coding=utf-8


class BST:
    class __Node:
        def __init__(self, element=None, left=None, right=None):
            self.e = element
            self.left = left
            self.right = right
    """
    时间复杂度分析：
    添加操作：addLast(e):O(n)    addFirst(e):O(1)    add(index, e):O(n/2)=O(n)
    删除操作：removeLast(e):O(n)    removeFirst(e):O(1)    remove(index, e):O(n/2)=O(n)
    修改操作：set(index, e):O(n)
    查找操作：get(index):O(n)    contains(e):O(n)
    """
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

    # 向二分搜索树中添加元素e
    def add(self, e):
        self.__root = self.__add(self.__root, e)

    # 向以node为根节点的二分搜索树中添加元素e，递归算法
    # 返回插入新节点后二分搜索树的根
    def __add(self, node, e):
        if node == None:
            self.__size += 1
            return self.__Node(element=e)

        if e < node.e:
            node.left = self.__add(node.left, e)
        elif e > node.e:
            node.right = self.__add(node.right, e)

        return node

    # 看二分搜索树中是否包含元素e
    def contains(self, e):
        return self.__contains(self.__root, e)

    # 看以node为根的二分搜索树中是否包含元素e，递归算法
    def __contains(self, node, e):
        if node == None:
            return False

        if e == node.e:
            return True
        elif e < node.e:
            return self.__contains(node.left, e)
        else:  # e > node.e
            return self.__contains(node.right, e)

    # 二分搜索树的前序遍历
    def preOrder(self):
        self.__preOrder(self.__root)

    # 前序遍历以node为根的二分搜索树，递归算法
    def __preOrder(self, node):
        if node == None:
            return

        print(node.e)
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    # 二分搜索树的中序遍历
    def inOrder(self):
        self.__inOrder(self.__root)

    # 中序遍历以node为根的二分搜索树，递归算法
    def __inOrder(self, node):
        if node == None:
            return

        self.__inOrder(node.left)
        print(node.e)
        self.__inOrder(node.right)

    # 二分搜索树的后序遍历
    def postOrder(self):
        self.__postOrder(self.__root)

    # 后序遍历以node为根的二分搜索树，递归算法
    def __postOrder(self, node):
        if node == None:
            return

        self.__postOrder(node.left)
        self.__postOrder(node.right)
        print(node.e)

    def __str__(self):
        self.__generateBSTString(self.__root, 0)
        return self.__treeString

    # 生成以node为根节点，深度为depth的描述二叉树的字符串
    def __generateBSTString(self, node, depth):
        if node == None:
            self.__treeString = self.__treeString + self.__generateDepthString(depth) + "null\n"
            return

        self.__treeString = self.__treeString + self.__generateDepthString(depth) + str(node.e) + "\n"
        self.__generateBSTString(node.left, depth + 1)
        self.__generateBSTString(node.right, depth + 1)

    def __generateDepthString(self, depth):
        res = ""
        for i in range(depth):
            res += "--"
        return res

