# coding=utf-8
import random
import time
from BasicDS.UFQuickFind import UFQuickFind
from BasicDS.UF import UF
from BasicDS.UFNumpy import UFNumpy


def testUF(uf, m):
    size = uf.getSize()

    startTime = time.time()
    for i in range(m):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
        uf.unionElements(a, b)
    for i in range(m):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
        uf.isConnected(a, b)
    endTime = time.time()

    return endTime - startTime


if __name__ == "__main__":
    size = 10000
    m = 100000

    # uf1 = UFQuickFind(size)
    # print("UFQuickFind : ", testUF(uf1, m), " s")

    uf2 = UF(size)
    print("UF : ", testUF(uf2, m), " s")

    uf3 = UFNumpy(size)
    print("UFNumpy : ", testUF(uf3, m), " s")


