# coding=utf-8
from BasicDS.LinkedListStack import LinkedListStack
from BasicDS.LinkedListQueue import LinkedListQueue


class BST:
    class __Node:
        def __init__(self, element=None, left=None, right=None):
            self.e = element
            self.left = left
            self.right = right
    """
    时间复杂度分析：
    添加操作：
    删除操作：
    修改操作：
    查找操作：
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

    # 二分搜索树的前序遍历的非递归实现
    def preOrderNR(self):
        if self.__root == None:
            return

        stack = LinkedListStack()
        stack.push(self.__root)
        while not stack.isEmpty():
            cur = stack.pop()
            print(cur.e)

            if cur.right != None:
                stack.push(cur.right)
            if cur.left != None:
                stack.push(cur.left)

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

    # 二分搜索树的层序遍历
    def levelOrder(self):
        if self.__root == None:
            return

        queue = LinkedListQueue()
        queue.enqueue(self.__root)
        while not queue.isEmpty():
            cur = queue.dequeue()
            print(cur.e)
            if cur.left != None:
                queue.enqueue(cur.left)
            if cur.right != None:
                queue.enqueue(cur.right)

    # 寻找二分搜索树中的最小元素
    def minimum(self):
        assert not (self.__size == 0), "BST is empty!"
        return self.__minimum(self.__root).e

    # 返回以node为根的二分搜索树的最小值所在的节点，递归算法
    def __minimum(self, node):
        if node.left == None:
            return node
        return self.__minimum(node.left)

    # 寻找二分搜索树中的最大元素
    def maximum(self):
        assert not (self.__size == 0), "BST is empty!"
        return self.__maximum(self.__root).e

    # 返回以node为根的二分搜索树的最大值所在的节点，递归算法
    def __maximum(self, node):
        if node.right == None:
            return node
        return self.__maximum(node.right)

    # 从二分搜索树中删除最小值所在的节点，返回最小值
    def removeMin(self):
        ret = self.minimum()
        self.__root = self.__removeMin(self.__root)
        return ret

    # 删除以node为根的二分搜索树中的最小节点
    # 返回删除节点后新的二分搜索树的根
    def __removeMin(self, node):
        if node.left == None:
            rightNode = node.right
            # node.right = None
            del node
            self.__size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    # 从二分搜索树中删除最大值所在的节点，返回最小值
    def removeMax(self):
        ret = self.maximum()
        self.__root = self.__removeMax(self.__root)
        return ret

    # 删除以node为根的二分搜索树中的最大节点
    # 返回删除节点后新的二分搜索树的根
    def __removeMax(self, node):
        if node.right == None:
            leftNode = node.left
            # node.left = None
            del node
            self.__size -= 1
            return leftNode
        node.right = self.__removeMax(node.right)
        return node

    # 从二分搜索树中删除元素为e的节点
    def remove(self, e):
        self.__root = self.__remove(self.__root, e)

    # 从二分搜索树中删除元素为e的节点，递归算法
    # 返回删除节点后新的二分搜索树的根
    def __remove(self, node, e):
        if node == None:
            return None

        if e < node.e:
            node.left = self.__remove(node.left, e)
            return node
        elif e > node.e:
            node.right = self.__remove(node.right, e)
            return node
        else:  # e == node.e
            # 待删除节点左子树为空的情况
            if node.left == None:
                rightNode = node.right
                # node.right = None
                del node
                self.__size -= 1
                return rightNode
            # 待删除节点右子树为空的情况
            if node.right == None:
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

    def __str__(self):
        self.__treeString = ""
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

