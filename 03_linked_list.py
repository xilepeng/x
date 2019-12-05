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

    # def reverse(self):
    #     """反转链表(迭代)
    #     [root] -> [curnode] -> [nextnode]
    #     [prevnode = None] <- [curnode]
    #     """
    #     curnode = self.root.next
    #     self.tailnode = curnode
    #     prevnode = None

    #     while curnode:
    #         nextnode = curnode.next
    #         curnode.next = prevnode

    #         if nextnode is None:
    #             self.root.next = curnode
            
    #         prevnode = curnode
    #         curnode = nextnode
    def reverse(self):
        """反转链表"""
        curnode = self.root.next
        self.tailnode = curnode  # 记得更新 tailnode，多了这个属性处理起来经常忘记
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode

def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(1) == 1
    assert ll.find(-1) == -1
    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert len(ll) == 3
    assert list(ll) == [1, 2, 3]
    # assert ll.find(0) == -1

    print(list(ll))


if __name__ == "__main__":
    test_linked_list()

