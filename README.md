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

* Example 1:

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建动态数组，仅演示使用，python中list完全能实现该功能
    array = Array()
    # array尾部添加三个元素
    array.addLast(13)
    array.addLast(14)
    array.addFirst(521)
    print(array)
    # array头部添加三个元素
    for i in range(8):
        array.addFirst(i + 12)
    print(array)
    # 指定位置添加元素
    array.add(8, "my dear")
    print(array)
    # 删除指定索引的元素
    for i in range(6):
        array.remove(0)  # 相当于array.removeFirst()
    print(array)
    # 删除指定值的某元素
    array.removeElement(12)
    print(array)
    print()
    # 判断是否包含某元素
    print("array contains 521 : ", array.contains(521))
    # 获取array元素的个数
    print("The size of array : ", array.getSize())
    # 判断队列是否为空
    print("array is empty : ", array.isEmpty())
```

`result:`

Array: size = 3 , capacity = 10

[521, 13, 14]

Array: size = 11 , capacity = 20

[19, 18, 17, 16, 15, 14, 13, 12, 521, 13, 14]

Array: size = 12 , capacity = 20

[19, 18, 17, 16, 15, 14, 13, 12, my dear, 521, 13, 14]

Array: size = 6 , capacity = 20

[13, 12, my dear, 521, 13, 14]

Array: size = 5 , capacity = 10

[13, my dear, 521, 13, 14]



array contains 521 :  True

The size of array :  5

array is empty :  False

* Example k:

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建队列
    queue = ArrayQueue()
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

`result:`

queue is empty :  True

ArrayQueue: front [13, 14] tail

The size of queue :  2

The front of queue :  13

ArrayQueue: front [14] tail