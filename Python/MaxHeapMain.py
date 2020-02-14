# coding=utf-8
import sys
import random
import time
from BasicDS.MaxHeap import MaxHeap

def testHeap(testData, isHeapify):
    startTime = time.time()

    if isHeapify:
        maxHeap = MaxHeap(arr=testData)
    else:
        maxHeap = MaxHeap()
        for num in testData:
            maxHeap.add(num)

    arr = []
    for i in range(len(testData)):
        arr.append(maxHeap.extractMax())
    for i in range(1, len(testData)):
        if arr[i - 1] < arr[i]:
            raise Exception("Error")
    print("Test MaxHeap completed.")

    endTime = time.time()
    return endTime - startTime


if __name__ == "__main__":
    n = 20000

    testData = [random.randint(0, sys.maxsize) for _ in range(n)]

    time1 = testHeap(testData, False)
    print("Without heapify: ", time1, "s")

    time2 = testHeap(testData, True)
    print("With heapify: ", time2, " s")

