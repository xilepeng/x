class Node(object):
    # 如果节点很多，我们可以用 __slots__ 来节省内存，把属性保存在一个 tuple 而不是 dict 里
    __slots__ = ('value', 'prev', 'next')   # save memory

    def __init__(self, value = None, prev = None, next = None):
        self.value, self.prev, self.next = value, prev, next

class CircularDoubleLinkedList(object):
    """
    循环双端链表 ADT
    多了个循环其实是把 root 的 prev 指向 tail 节点，串起来
    """
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0
    def __len__(self):
        return self.length
    def headnode(self):
        return self.root.next
    def tailnode(self):
        return self.root.prev
    
    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('Full')
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('Full')
        node = Node(value=value)

        if self.root.next is self.root: # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            self.root.next = node
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode
    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev    # tailnode
        while curnode is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

def test_double_link_list():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]
    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove(headnode)    # O(1) remove
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]




    
