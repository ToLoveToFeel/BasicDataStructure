from BasicDS.LinkedListQueue import LinkedListQueue

if __name__ == "__main__":
    queue = LinkedListQueue()

    for i in range(10):
        queue.enqueue(i)
        print(queue)
        if i % 3 == 2:
            queue.dequeue()
            print(queue)
