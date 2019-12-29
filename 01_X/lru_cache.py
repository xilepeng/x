
def cache(func):
    data = {}

    def wrapper(n):
        if n in data:
            return data[n]
        else:
            res = func(n) #调用原来函数计算
            data[n] = res
            return res
    return wrapper


class  Node(object):
    def __init__(self, prev = None, next = None, key = None, value = None):
        self.prev, self.next, self.key, self.value = prev, next, key, value

class CircularDoubleLinkedList(object):
    def __init__(self):
        node = Node()
        node.prev, node.next = node, node
        self.rootnode = node

    def headnode(self):
        return self.rootnode.next

    def tailnode(self):
        return self.rootnode.prev

    def remove(self, node):
        if node is self.rootnode:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def append(self, node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.next = self.rootnode
        self.rootnode.prev = node

class LRUCache(object):
    def __init__(self,maxsize= 16):
        self.maxsize = maxsize
        self.code = {}  #缓存计算出来的结果
        self.access = CircularDoubleLinkedList()    #把访问的key记录下来
        self.isfull = len(self.cache) >= self.maxsize

    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get()
            if cachenode is not None:   #hit 命中缓存
                self.access.remove(cachenode)
                self.access.append(cachenode)
                return cachenode.value
            else: #miss
                result = func(n) #没有满，计算结果值
                if not self.isfull:
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode, self.access.rootnode, n, value)
                    self.cache[n] = newnode

                    self.isfull = len(self.cache) >= self.maxsize
                    return value
                else: #full
                    lru_node = self.access.headnode()
                    del self.cache[lru_node.key]
                    self.access.remove(lru_node)
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode, self.access.rootnode, n, value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                return value
        return wrapper


@LRUCache
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 10):
    print(fib(i))






# 内存不够用
# lru 把最早访问的删除
# lfu 把最少访问的删除
# 


# def cache(func):
#     data = {}

#     def wrapper(n):
#         if n in data:
#             return data[n]
#         else:
#             res = func(n) #调用原来函数计算
#             data[n] = res
#             return res
#     return wrapper

# @cache
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# for i in range(1, 10):
#     print(fib(i))




# from functools import lru_cache
#
# @lru_cache()
# def add(x, y):
#     print("函数被调用运行: {} + {}" .format(x, y))
#     return x + y
#
# if __name__=='__main__':
#     print(add(1, 2))
#     print('*'*20)
#     print(add(1, 2))
#     print('*'*20)
#     print(add(1, 3))