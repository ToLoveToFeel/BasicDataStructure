from BasicDS.ArrayStack import ArrayStack

if __name__ == "__main__":
    stack = ArrayStack()

    for i in range(5):
        stack.push(i)
        print(stack)

    stack.pop()
    print(stack)


