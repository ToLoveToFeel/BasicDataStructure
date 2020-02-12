from BasicDS.Arrays import Array

if __name__ == "__main__":
    # arr = Array(20, "int")
    # arr = Array(20, "np.float")
    arr = Array(dtype="np.float")
    for i in range(10):
        arr.addLast(i)
    print(arr)

    arr.addLast(9)
    arr.addLast(16)
    print(arr)

    arr.removeFirst()
    arr.removeFirst()
    print(arr)




