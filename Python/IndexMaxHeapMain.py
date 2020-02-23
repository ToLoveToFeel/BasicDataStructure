# coding=utf-8
from BasicDS.IndexMaxHeap import IndexMaxHeap


if __name__ == "__main__":
    arr = [15, 17, 19, 13, 22, 16, 28, 30, 41, 62]
    # 创建最大索引堆
    indexMaxHeap = IndexMaxHeap(capacity=len(arr))
    # 最大索引堆中添加数据
    for i in range(len(arr)):
        indexMaxHeap.add(i, arr[i])
    # 获取并删除最大索引堆中最大值
    print("Max value : ", indexMaxHeap.extractMax())
    # 仅仅获取最大值
    print("Max value after delete max : ", indexMaxHeap.findMax())
    # 将最大值替换为-1
    indexMaxHeap.replace(-1)
    # 重新查看最大值
    print("Max value after replace max with -1 : ", indexMaxHeap.findMax())
    # 获取最大值的索引
    print("The index of max value : ", indexMaxHeap.findMaxIndex())
    # 判断索引为9的位置在最大索引堆中是否存在
    print("IndexMaxHeap has value in index 9 : ", indexMaxHeap.contains(9))
    # # 获取arr[9]对应的数据，应为已经删除所以会出错
    # print(indexMaxHeap.getItem(9))
    print("The value where index is 8 : ", indexMaxHeap.getItem(8))
    # 获取索引堆的大小
    print("The size of IndexMaxHeap : ", indexMaxHeap.getSize())

