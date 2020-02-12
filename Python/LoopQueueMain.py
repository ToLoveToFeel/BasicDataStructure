from BasicDS.LoopQueue import LoopQueue

if __name__ == "__main__":
    queue = LoopQueue()

    for i in range(10):
        queue.enqueue(i)
        print(queue)
        if i % 3 == 2:
            queue.dequeue()
            print(queue)
