from BasicDS.Array import Array

if __name__ == "__main__":
    # arr = Array(20)
    # arr = Array(arr=[1,2,3,4])
    arr = Array()
    for i in range(9):
        arr.addLast(i)
    print(arr)

    arr.addLast(9)
    print(arr)
    arr.addLast(16)
    print(arr)

    arr.removeFirst()
    print(arr)
    arr.removeFirst()
    arr.removeLast()
    arr.removeFirst()
    arr.removeFirst()
    print(arr)
    arr.removeFirst()
    print(arr)





