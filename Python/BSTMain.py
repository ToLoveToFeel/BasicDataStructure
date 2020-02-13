# coding=utf-8
from BasicDS.BST import BST
import random
from BasicDS.Arrays import Array

if __name__ == "__main__":
    bst = BST()
    # nums = [5, 3, 6, 8, 4, 2]
    # for num in nums:
    #     bst.add(num)
    ###########################
    #            5            #
    #          /   \          #
    #        3      6         #
    #      /  \      \        #
    #    2     4      8       #
    ###########################
    # # 各种遍历
    # print(bst)
    # bst.preOrder()
    # print()
    # bst.preOrderNR()
    # print()
    # bst.inOrder()
    # print()
    # bst.postOrder()
    # bst.levelOrder()
    
    # 测试删除最小值，最大值
    for i in range(1000):
        bst.add(random.randint(0, 1000))

    nums = Array()
    while not bst.isEmpty():
        nums.addLast(bst.removeMax())
    print(nums)
    for i in range(1, nums.getSize()):
        if nums.get(i - 1) < nums.get(i):
            raise Exception("Error")


