from BasicDS.LinkedList import LinkedList

if __name__ == "__main__":
    linkedList = LinkedList()
    for i in range(5):
        linkedList.addFirst(i)
        print(linkedList)

    linkedList.add(2, 666)
    print(linkedList)

    linkedList.remove(2)
    print(linkedList)

    linkedList.removeFirst()
    print(linkedList)

    linkedList.removeLast()
    print(linkedList)



