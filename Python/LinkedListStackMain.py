from BasicDS.LinkedListStack import LinkedListStack

if __name__ == "__main__":
    stack = LinkedListStack()

    for i in range(5):
        stack.push(i)
        print(stack)

    stack.pop()
    print(stack)


