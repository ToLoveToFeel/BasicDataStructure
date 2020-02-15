# coding=utf-8
from BasicDS.SegmentTree import SegmentTree


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    segTree = SegmentTree(arr=nums, merger=(lambda a, b: a + b))
    print(segTree)
    print(segTree.query(0, 2))
    print(segTree.query(2, 5))
    print(segTree.query(0, 5))
    segTree.set(1, 1)
    print(segTree.query(0, 2))

