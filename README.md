# BasicDS

### Introduction

Data Structure realized with Python.

---

### How to install?

Download the BasicDS-0.0.1.whl file, then enter the directory where the BasicDS-0.0.1.whl file is. Finally you can install the package with the command:

```
pip install BasicDS-0.0.1.whl
```

Next, you can use the package.

---

### Data structure catalog

* Array，ArrayQueue，ArrayStack
* LoopQueue
* LinkedList，LinkedListStack，LinkedListQueue，LinkedListSet，LinkedListMap
* BST，BSTSet，BSTMap
* MaxHeap，MinHeap，PriorityQueue
* SegmentTree
* Trie
* UFQuickFind，UF
* AVLTree，AVLTreeSet，AVLTreeMap
* RBTree
* HashTable，HashSet，HashMap

![img](https://github.com/i-love-linux/BasicDataStructure/blob/master/BasicDS.png)

---

### How to use?

* Example 1:（动态数组Array）

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

* Example 2:（栈Stack）

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建栈
    # stack = LinkedListStack()
    stack = ArrayStack()
    # 入栈五个元素
    for i in range(5):
        stack.push(i + 17)
    print(stack)
    # 出队一个元素
    stack.pop()
    print(stack)
    # 获取栈的大小
    print("The size of stack : ", stack.getSize())
    # 查看栈顶元素
    print("The peek of stack : ", stack.peek())
    # 判断栈是否为空
    print("stack is empty : ", stack.isEmpty())
```

`result:`

ArrayStack: [17, 18, 19, 20, 21] top

ArrayStack: [17, 18, 19, 20] top

The size of stack :  4

The peek of stack :  20

stack is empty :  False

* Example 3:（队列Queue）

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建队列
    # queue = LinkedListQueue()
    # queue = LoopQueue()
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

* Example 4:（集合Set）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据，5个不同的数据
    # 出现次数："my":2，"dear":3，"is":1，"you"：2，"!":1
    data = ["my", "dear", "is", "you", "!", "dear", "my", "dear", "you"]
    # 创建集合
    # set = BSTSet()
    # set = AVLTreeSet()
    # set = HashSet()
    set = LinkedListSet()
    # 向集合中添加元素
    for word in data:
        set.add(word)
    # 查看集合中是否包含"my"
    print("set contains \"my\" : ", set.contains("my"))
    # 从集合中删除"my"
    set.remove("my")
    # 获取集合的大小
    print("The size of set : ", set.getSize())
    # 查看集合中是否包含"my"
    print("set contains \"my\" after delete \"my\" : ", set.contains("my"))
    # 判断集合是否为空
    print("set is empty : ", set.isEmpty())
```

`result:`

set contains "my" :  True

The size of set :  4

set contains "my" after delete "my" :  False

set is empty :  False

* Example 5:（映射Map）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据，5个不同的数据
    # 出现次数："my":2，"dear":3，"is":1，"you"：2，"!":1
    data = ["my", "dear", "is", "you", "!", "dear", "my", "dear", "you"]
    # 创建映射
    # map = BSTMap()
    # map = AVLTreeMap()
    # map = HashMap()
    map = LinkedListMap()
    # 向映射中添加元素
    for word in data:
        if map.contains(word):
            map.add(word, map.get(word) + 1)
        else:
            map.add(word, 1)
    # 查看映射中是否包含"my"
    print("map contains \"my\" : ", map.contains("my"))
    # 从映射中删除"my"
    map.remove("my")
    # 获取映射的大小
    print("The size of map : ", map.getSize())
    # 查看映射中是否包含"my"
    print("map contains \"my\" after delete \"my\" : ", map.contains("my"))
    # 判断映射是否为空
    print("map is empty : ", map.isEmpty())
    # 查看"dear"出现的次数
    print("\"dear\" appears : ", map.get("dear"), " times.")
```

`result:`

map contains "my" :  True

The size of map :  4

map contains "my" after delete "my" :  False

map is empty :  False

"dear" appears :  3  times.

* Example 6:（堆Heap）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据
    data = [25, 37, 22, 21, 29, 34]
    # 创建并查集，含有10个元素：0~9
    # maxHeap = MaxHeap()  # 默认堆为空
    maxHeap = MaxHeap(arr=data)  # 会利用heapify创建堆
    # 取出堆中最大元素
    print("The max value of heap : ", maxHeap.extractMax())
    # 获取堆的大小
    print("The size of heap :", maxHeap.getSize())
    # 查看堆中最大元素
    print("The max value of heap after extractMax : ", maxHeap.findMax())
    # 替换堆中最大元素
    maxHeap.replace(-1)
    print("The max value of heap after replace max with -1 : ", maxHeap.findMax())
    # 判断堆中是否为空
    print("heap is empty : ", maxHeap.isEmpty())
    # 向堆中添加一个元素
    maxHeap.add(1314)
    print("The size of heap after add 1314 : ", maxHeap.getSize())
```

`result:`

The max value of heap :  37

The size of heap : 5

The max value of heap after extractMax :  34

The max value of heap after replace max with -1 :  29

heap is empty :  False

The size of heap after add 1314 :  6

* Example 7:（优先队列PriorityQueue）

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建优先队列，默认出队出最大值，isMaxHeap=False出队最小值
    queue = PriorityQueue(isMaxHeap=False)
    # 判断队列是否为空
    print("queue is empty : ", queue.isEmpty())
    # 入队三个元素
    queue.enqueue(66)
    queue.enqueue(27)
    queue.enqueue(35)
    # 获取队列元素的个数
    print("The size of queue : ", queue.getSize())
    # 查看队首的元素，不出队
    print("The front of queue : ", queue.getFront())
    # 出队一个元素，同时返回队首元素
    print("dequeue element : ", queue.dequeue())
```

`result:`

queue is empty :  True

The size of queue :  3

The front of queue :  27

dequeue element :  27

* Example 8:（线段树Segment）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据
    nums = [-2, 0, 3, -5]
    # 创建线段树
    segTree = SegmentTree(arr=nums, merger=(lambda a, b: a + b))
    print("segTree is :", segTree)
    # 查询数组nums索引在[0...2]范围的和，因为merger为+
    print("[0...2] :", segTree.query(0, 2))
    # 将数组nums[1]更新为1
    segTree.set(1, 1)
    # 查询线段树索引在[0...2]范围的和，因为merger为+
    print("[0...2] after update :", segTree.query(0, 2))
```

`result:`

segTree is : [-4, -2, -2, -2, 0, 3, -5, None, None, None, None, None, None, None, None, None]

[0...2] : 1

[0...2] after update : 2

* Example 9:（字典树Trie）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据，5个不同的数据
    # 出现次数："my":2，"dear":3，"is":1，"you"：2，"!":1
    data = ["my", "dear", "is", "you", "!", "dear", "my", "dear", "you"]
    # 创建Trie
    trie = Trie()
    # 向Trie中添加元素
    for word in data:
        trie.add(word)
    # 获取Trie的大小
    print("The size of trie : ", trie.getSize())
    # 查看Trie中是否包含"my"
    print("trie contains \"my\" : ", trie.contains("my"))
    # 查看Trie中是否包含前缀"de"
    print("trie contains Prefix \"de\" : ", trie.isPrefix("de"))
    # 判断Trie是否为空
    print("trie is empty : ", trie.isEmpty())
```

`result:`

The size of trie :  5

trie contains "my" :  True

trie contains Prefix "de" :  True

trie is empty :  False

* Example 10:（并查集Union Find）

```python
from BasicDS import *

if __name__ == "__main__":
    # 创建并查集，含有10个元素：0~9
    uf = UF(size=10)
    # 合并某两个集合
    uf.unionElements(0, 1)
    uf.unionElements(0, 2)
    uf.unionElements(0, 3)
    # 获取并查集的大小
    print("The size of uf : ", uf.getSize())
    # 判断某两个元素是否在同一个集合中
    print("Element 1 and element 3 in a set : ", uf.isConnected(1, 3))
    print("Element 1 and element 6 in a set : ", uf.isConnected(1, 6))
```

`result:`

The size of uf :  10

Element 1 and element 3 in a set :  True

Element 1 and element 6 in a set :  False

* Example 11:（红黑树RBTree）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据，5个不同的数据
    # 出现次数："my":2，"dear":3，"is":1，"you"：2，"!":1
    data = ["my", "dear", "is", "you", "!", "dear", "my", "dear", "you"]
    # 创建映射
    rbt = RBTree()
    # 向映射中添加元素
    for word in data:
        if rbt.contains(word):
            rbt.add(word, rbt.get(word) + 1)
        else:
            rbt.add(word, 1)
    # 查看映射中是否包含"my"
    print("rbt contains \"my\" : ", rbt.contains("my"))
    # 获取映射的大小
    print("The size of rbt : ", rbt.getSize())
    # 判断映射是否为空
    print("rbt is empty : ", rbt.isEmpty())
    # 查看"dear"出现的次数
    print("\"dear\" appears : ", rbt.get("dear"), " times.")
```

`result:`

rbt contains "my" :  True

The size of rbt :  5

rbt is empty :  False

"dear" appears :  3  times.

* Example 12:（哈希表HashTable）

```python
from BasicDS import *

if __name__ == "__main__":
    # 需要处理的数据，5个不同的数据
    # 出现次数："my":2，"dear":3，"is":1，"you"：2，"!":1
    data = ["my", "dear", "is", "you", "!", "dear", "my", "dear", "you"]
    # 创建映射
    map = HashTable()
    # 向映射中添加元素
    for word in data:
        if map.contains(word):
            map.add(word, map.get(word) + 1)
        else:
            map.add(word, 1)
    # 查看映射中是否包含"my"
    print("map contains \"my\" : ", map.contains("my"))
    # 从映射中删除"my"
    map.remove("my")
    # 获取映射的大小
    print("The size of map : ", map.getSize())
    # 查看映射中是否包含"my"
    print("map contains \"my\" after delete \"my\" : ", map.contains("my"))
    # 判断映射是否为空
    print("map is empty : ", map.isEmpty())
    # 查看"dear"出现的次数
    print("\"dear\" appears : ", map.get("dear"), " times.")
```

`result:`

map contains "my" :  True

The size of map :  4

map contains "my" after delete "my" :  False

map is empty :  False

"dear" appears :  3  times.