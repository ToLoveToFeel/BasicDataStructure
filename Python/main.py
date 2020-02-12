from BasicDS.Arrays import Array
import numpy as np

if __name__ == "__main__":
    arr = Array(20)
    for i in range(10):
        arr.addLast(i)
    print(arr)
    arr.removeElement(4)
    arr.removeFirst()
    print(arr)



