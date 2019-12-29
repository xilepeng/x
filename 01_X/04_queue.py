from collections import deque

class Node(object):
    """Node
    [value / next]
    """
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None

class LinkedList(object):
    """链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        """ [node]
         if tailnode is None:
            [root] -> [None]   [tailnode] -> None
            [root] -> [node] <- self.tailnode
         else:
            [root] -> [node0] -> [tailnode] <- self.tailnode
            [root] -> [node0] -> [tailnode] -> [node] <- self.tailnode 
        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)  # 新建节点
        tailnode = self.tailnode    # 防止丢失下一个数据
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        """
        [self.root] -> [None]  [self.tailnode] -> None
        [self.root] -> [node] <- self.tailnode

        [root] ->[node0] <- [headnode]
        [root] -> [node] -> [node0]

        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    
    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def remove(self, value):
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                if curnode is self.tailnode:
                    if prevnode == self.root:
                        prevnode = None
                    else:
                        prevnode.next = curnode.next
                del curnode
                self.length -= 1
                return 1    # 表明删除成功         
            else:
                prevnode = curnode
        return -1

    def find(self, value):
        index = 0
        for node in self.iter_node():   # 我们定义了 __iter__， 这里就可以用 for 遍历他了
            if node.value == value:
                return index
            index += 1
        return -1
    
    def popleft(self):
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        self.length -= 1

        if headnode is self.tailnode:
            self.tailnode = None
            # self.root.next = None
        del headnode 
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tailnode = None
        self.length = 0



#####################################
# Queue实现
#####################################
class EmptyError(Exception):
    """自定义异常"""
    pass

class Queue(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()
    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):  # O(1)
        """队尾添加元素"""
        return self._item_linked_list.append(value)
    
    def pop(self):
        """队头删除元素"""
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_linked_list.popleft()

def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)
    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

class MyQueue:
    """使用 collections.deque 可以迅速实现一个队列"""
    def __init__(self):
        self.items = deque()
    
    def append(self, val):
        return self.items.append(val)

    def pop(self, val):
        return self.items.appendleft(val)

    def __len__(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]


if __name__ == "__main__":
    test_queue()

