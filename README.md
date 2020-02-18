# BasicDS

### Introduction

Data Structure realized with Python.

---

### How to install?

Just download the .whl file, then enter the directory. Finally you can install the package with the command:

```
pip install BasicDS-0.0.1.whl
```

Next, you can use the package.

---

### Data structure catalog

* Array，ArrayQueue，ArrayStack

* LinkedList，LinkedListStack，LinkedListQueue，LinkedListSet，LinkedListMap
* LoopQueue
* BST，BSTSet，BSTMap
* AVLTree，AVLTreeMap，AVLTreeSet
* MaxHeap，MinHeap，PriorityQueue
* SegmentTree
* Trie
* UFQuickFind，UF
* RBTree
* HashTable，HashSet，HashMap

---

### How to use?

`Example 1:`

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建队列
    queue = LinkedListQueue()
    # 判断队列是否为空
    print("queue is empty : ", queue.isEmpty())
    # 入队两个元素
    queue.enqueue(13)
    queue.enqueue(14)
    print(queue)
    # 获取队列元素的个数
    print("The size of queue : ", queue.getSize())
    # 查看队首的元素，不出队
    print("The front of queue : ", queue.getFront())
    # 出队一个元素，同时返回队首元素
    queue.dequeue()
    print(queue)
```





