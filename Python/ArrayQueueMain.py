from BasicDS.ArrayQueue import ArrayQueue

if __name__ == "__main__":
    stack = ArrayQueue()

    for i in range(5):
        stack.enqueue(i)
        print(stack)

    stack.dequeue()
    print(stack)


