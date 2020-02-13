# coding=utf-8
from BasicDS.BST import BST

if __name__ == "__main__":
    bst = BST()
    nums = [5, 3, 6, 8, 4, 2]
    for num in nums:
        bst.add(num)
    ###########################
    #            5            #
    #          /   \          #
    #        3      6         #
    #      /  \      \        #
    #    2     4      8       #
    ###########################
    # print(bst)
    # bst.preOrder()
    # print()
    # bst.preOrderNR()
    # print()
    # bst.inOrder()
    # print()
    # bst.postOrder()
    bst.levelOrder()


