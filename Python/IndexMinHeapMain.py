# coding=utf-8
from BasicDS.IndexMinHeap import IndexMinHeap


if __name__ == "__main__":
    arr = [15, 17, 19, 13, 22, 16, 28, 30, 41, 62]
    # 创建最大索引堆
    indexMinHeap = IndexMinHeap(capacity=len(arr))
    # 最大索引堆中添加数据
    for i in range(len(arr)):
        indexMinHeap.add(i, arr[i])
    # 获取并删除最大索引堆中最大值
    print("Min value : ", indexMinHeap.extractMin())
    # 仅仅获取最小值
    print("Min value after delete min : ", indexMinHeap.findMin())
    # 将最小值替换为100
    indexMinHeap.replace(100)
    # 重新查看最小值
    print("Min value after replace min with 100 : ", indexMinHeap.findMin())
    # 获取最小值的索引
    print("The index of min value : ", indexMinHeap.findMinIndex())
    # 判断索引为3的位置在最小索引堆中是否存在
    print("IndexMinHeap has value in index 3 : ", indexMinHeap.contains(3))
    # # 获取arr[3]对应的数据，应为已经删除所以会出错
    # print(indexMinHeap.getItem(3))
    print("The value where index is 0 : ", indexMinHeap.getItem(0))
    # 获取索引堆的大小
    print("The size of IndexMinHeap : ", indexMinHeap.getSize())

