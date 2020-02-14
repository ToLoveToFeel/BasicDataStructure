# coding=utf-8
import sys
import random
from BasicDS.MaxHeap import MaxHeap


if __name__ == "__main__":
    n = 10000

    maxHeap = MaxHeap()
    for i in range(n):
        maxHeap.add(random.randint(0, sys.maxsize))

    arr = []
    for i in range(n):
        arr.append(maxHeap.extractMax())

    for i in range(1, n):
        if arr[i-1] < arr[i]:
            raise Exception("Error")

    print("Test MaxHeap completed.")



